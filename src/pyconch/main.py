"""
main entry point to the program
"""


from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout
from ptterm import Terminal
from pytconf import config_arg_parse_and_launch, register_endpoint, register_main

from pyconch.static import APP_NAME, DESCRIPTION, VERSION_STR


@register_endpoint(
    description="Run a terminal",
)
def term():
    def done():
        application.exit()

    application = Application(
        layout=Layout(
            container=Terminal(done_callback=done)
        ),
        full_screen=True,
    )
    application.run()


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    config_arg_parse_and_launch()


if __name__ == "__main__":
    main()
