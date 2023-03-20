"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc

from pcconfig import config

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


def index():
    return pc.center(
        pc.vstack(
            pc.heading("E-Hotel Service", font_size="2em"),
            pc.box("by Mershab Issadien"),
            pc.box("Links:",
                   pc.link(
                       pc.button("counter"),
                       href="/counter",
                       color="rgb(107,99,246)",
                       button=True,
                   ),
                   pc.link(
                       pc.button("test"),
                       href="/test",
                       color="rgb(107,99,246)",
                       button=True,
                   ),
                   pc.link(
                       pc.button("Search"),
                       href="/search",
                       color="rgb(107,99,246)",
                       button=True,
                   ),
                   spacing="1.5em",
                   font_size="2em",
               )
        ),
        padding_top="10%",
    )
