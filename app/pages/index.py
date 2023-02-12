"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc

from pcconfig import config

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


def index():
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone!", font_size="2em"),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            pc.link(
                pc.button("counter"),
                href="/counter",
                color="rgb(107,99,246)",
                button=True,
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )
