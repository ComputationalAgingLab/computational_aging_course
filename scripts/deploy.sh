#!/usr/bin/env bash
# Build the book from scratch and publish it to GitHub Pages (the gh-pages branch).
#
# Usage: scripts/deploy.sh [--dry-run] [--skip-git-checks]
#   --dry-run          run the checks and the build, but do not publish
#   --skip-git-checks  do not require a clean 'main' in sync with origin (for testing a branch)
#
# The build fails on any Sphinx warning and on any notebook cell that raises.
# If a CNAME file exists in the repository root, its domain is published with the site.
set -euo pipefail

REMOTE=origin
BRANCH=main
SITE_URL="https://computationalaginglab.github.io/computational_aging_course"

dry_run=false
git_checks=true
for arg in "$@"; do
    case "$arg" in
        --dry-run) dry_run=true ;;
        --skip-git-checks) git_checks=false ;;
        -h|--help) sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *) echo "Unknown option: $arg (see --help)" >&2; exit 2 ;;
    esac
done

die() { echo "deploy: $*" >&2; exit 1; }
sha256() { if command -v sha256sum > /dev/null; then sha256sum; else shasum -a 256; fi | cut -d' ' -f1; }

cd "$(git rev-parse --show-toplevel)"
command -v uv >/dev/null || die "uv is not installed, see https://docs.astral.sh/uv/"

if $git_checks; then
    echo "==> Checking the repository state"
    [[ "$(git branch --show-current)" == "$BRANCH" ]] || die "switch to the '$BRANCH' branch first"
    [[ -z "$(git status --porcelain)" ]] || die "the working tree has uncommitted changes"
    git fetch --quiet "$REMOTE" "$BRANCH"
    [[ "$(git rev-parse HEAD)" == "$(git rev-parse "$REMOTE/$BRANCH")" ]] \
        || die "'$BRANCH' is not in sync with '$REMOTE/$BRANCH', pull or push first"
fi

echo "==> Installing the locked environment"
uv sync --locked

echo "==> Building the book (notebooks are executed, this takes a few minutes)"
uv run jupyter-book clean . > /dev/null
uv run jupyter-book build . --warningiserror --keep-going \
    || die "the build failed, see the messages above"
if [[ -d _build/html/reports ]] && [[ -n "$(ls -A _build/html/reports)" ]]; then
    die "some notebooks failed to execute, see _build/html/reports/"
fi

if $dry_run; then
    echo "==> Dry run: the book is built in _build/html and was not published"
    exit 0
fi

cname_args=()
if [[ -f CNAME ]]; then
    domain="$(tr -d '[:space:]' < CNAME)"
    cname_args=(--cname "$domain")
    SITE_URL="https://$domain"
fi

echo "==> Publishing to the gh-pages branch"
uv run ghp-import --no-jekyll --push --force --remote "$REMOTE" --branch gh-pages \
    --message "Deploy $(git rev-parse --short HEAD)" ${cname_args[@]+"${cname_args[@]}"} _build/html

# GitHub Pages needs a minute or two; the site is up to date once it serves our search index
echo "==> Waiting for $SITE_URL to update"
local_index="$(sha256 < _build/html/searchindex.js)"
for _ in $(seq 30); do
    remote_index="$(curl -fsSL "$SITE_URL/searchindex.js?nocache=$(date +%s)" 2> /dev/null | sha256)"
    if [[ "$remote_index" == "$local_index" ]]; then
        echo "==> Done: $SITE_URL/intro.html"
        exit 0
    fi
    sleep 10
done
echo "deploy: published, but $SITE_URL does not show the new version yet; check it in a few minutes" >&2
