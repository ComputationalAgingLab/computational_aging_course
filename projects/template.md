# Project report template

Think about the report as a research paper. Only text, references and pictures demonstrating the logic of your research. All code is placed in a separate notebook.

The report should contain three sections: Introduction, Results, Discussion. Feel free to use any additional style blocks from [jupyter_book](https://jupyterbook.org/en/stable/intro.html) API for making your report more beautiful.

Use single # for project title, ## for sections and ### for subsections of your report.

## Introduction

Describe your task and its background. Imagine that your potential employer will read this report. Try to use simple language for explaining your task and hypothesis but be precise in terms.

Create a separate bibtex file (`.bib` extension) to store the references. Any bibtex reference can be obtained from google scholar by clicking on `cite` button and choosing `bibtex` option. Use the following directive to cite something inside the text of your report {cite}`bibtex_citekey`. A useful bibtex guide is here [guide](https://www.bibtex.com/g/bibtex-format/).

## Results

This section is for presenting and describing your results. Put pictures, text, references, formulae and all that you need here. You are free to put code here also but it is quite redundant because you are also preparing the notebook with code and comments. 

Put mathematical formulae in the report if needed. Use, for example, the following directive for that

$$ y = wx + b$$

Put figures in your report. If some of the pictures were produced with python code, save them in a separate folder within the folder of your project. Use the following directive to put a figure inside the text:

```{figure} figs/hallmarks_taxonomy.png
:name: hallmarks_taxonomy
Hallmarks taxonomy.
```

Use the following directive to refer to a particular picture in the text {numref}`hallmarks_taxonomy`.

## Discussion

Discuss your results here and answer additional questions from questions/tasks section of **project proposal**. 

## Credits
This text prepared by [Team member 1](https://linktoyourprofile/scholar/or/linkedin.com) ...

## References

```{bibliography}
:style: plain
:filter: docname in docnames
```
