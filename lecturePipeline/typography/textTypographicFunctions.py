import manim

from lecturePipeline.typography.text import textHandler


def bodyCompact(input, width, config=manim.config):
    typo = "tokens.body-compact-02"
    return textHandler(input, typo, config, width)


def body(input, width, config=manim.config, number=1):
    typo = f"tokens.body-0{number}"
    return textHandler(input, typo, config, width)


def code(input, width, config=manim.config, number=1):
    typo = f"tokens.code-0{number}"
    return textHandler(input, typo, config, width)


def legal(input, width, config=manim.config, number=1):
    typo = f"tokens.legal-0{number}"
    return textHandler(input, typo, config, width)


def label(input, width, config=manim.config, number=1):
    typo = f"tokens.label-0{number}"
    return textHandler(input, typo, config, width)


def helperText(input, width, config=manim.config, number=1):
    typo = f"tokens.helper-text-0{number}"
    return textHandler(input, typo, config, width)


def headingCompact(input, width, config=manim.config, number=1):
    typo = f"tokens.heading-compact-0{number}"
    return textHandler(input, typo, config, width)


def heading(input, width, config=manim.config, number=1):
    typo = f"tokens.heading-0{number}"
    return textHandler(input, typo, config, width)


def fluidHeading(input, width, config=manim.config, number=1, size="mx"):
    typo = f"fluid.heading-{number}-{size}"
    return textHandler(input, typo, config, width)


def fluidParagraph(input, width, config=manim.config, number=1, size="mx"):
    typo = f"fluid.paragraph-{number}-{size}"
    return textHandler(input, typo, config, width)


def fluidQuote(input, width, config=manim.config, number=1, size="mx"):
    typo = f"fluid.quotation-{number}-{size}"
    return textHandler(input, typo, config, width)


def fluidDisplay(input, width, config=manim.config, number=1, size="mx"):
    typo = f"fluid.display-{number}-{size}"
    return textHandler(input, typo, config, width)
