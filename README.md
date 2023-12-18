[![DOI](https://zenodo.org/badge/519051051.svg)](https://zenodo.org/doi/10.5281/zenodo.10400595)
![made with love](https://img.shields.io/badge/made%20with%20%E2%9D%A4%EF%B8%8F-8A2BE2)

# Computational Biology of Aging book

This free open-access book is devoted to the best practices in the computational system biology of aging. If you are interested in reading please proceed to the [Book page](https://computationalaginglab.github.io/computational_aging_course/intro.html). Now this book is under development. If you want to contribute to this project, please read our short contribution remark below. If you have some questions feel free to write to this e-mail: <dmitrii.kriukov@skoltech.ru>.

## Abstract
This course is devoted to the study of key methods of computational biology of aging, which have had a significant impact on the field in recent years. We will take a detailed look at aging clock models, survival curves, Gompertz models, dynamical models as well as key aspects of the biology of aging (including its molecular part). Students will get experience in differential gene expression or methylation analysis in the context of aging, hazard ratio models fitting and interpretation, aging clocks construction and their exploration and develop an intuition in dynamical systems modeling. The course aims to form a systematic view of the biology of aging, and offer a holistic computational methodology for the study of this problem.


# How to contribute

If you want to contribute to this project, please follow this guide:
1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) Computational Biology of Aging book.
2. Set up the local repository:
    ```
    # Clone fork
    git clone https://github.com/{YOUR-USERNAME}/computational_aging_course.git
    cd computational_aging_course

    # Create Conda environment (alternatively you can use mamba distributive which is faster)
    conda env create -f environment.yml
    conda activate cba_course

    # Compile book
    jupyter-book build .
    ```
2. Choose a topic on computational aging biology where you have particular expertise.
3. Provide the following materials:
    * write a lecture text in markdown (or [MyST](https://jupyterbook.org/en/stable/content/myst.html)) format supplying it with images, videos and other embedded materials.
    * (recommended) prepare a jupyter notebook on some computational topic with clarification of the approach. Provide some code and necessary text, formulas, graphics as well as toy or real data examples of the approach application.
    * (would be great but not necessary) prepare a video with a presentation of your teaching materials. Actually, these materials should be a repetition of what you're saying in the markdown text or notebook. Please, attach also a link to your presentation - put it into your lecture text.
4. Commit your materials to your fork and make a pull request.
5. (optional) To make the process faster, write about your intention to contribute to this e-mail: <dmitrii.kriukov@skoltech.ru>
6. (optional) Modify `.toc.yml` file by adding the names of your chapters to a place you prefer. See [this guide](https://jupyterbook.org/en/stable/structure/configure.html?highlight=.toc#configure-all-entries-in-the-toc) for details.

If you found some mistakes or mistypes in the materials, or if you want to provide some important comments, please, issue this by pushing **issue** button on the corresponding page within the [Book](https://computationalaginglab.github.io/computational_aging_course/intro.html).


## How to add dependencies
We are trying to minimize dependencies, but if we need some, we just add them to the `environment.yml` file. Note, if you added some dependencies try to build your fork of the book by creating a new environment.

## Cite us 
```
@online{kriukov2023compagingbook,
  year={2023},
  author={Dmitrii Kriukov and Irina Zhegalova and Simon Steshin and Dmitrii Smirnov, Evgeniy Efimov, and Ekaterina Khrameeva},
  title={Computational Biology of Aging},
  url={https://computationalaginglab.github.io/computational_aging_course/intro.html},
}
```