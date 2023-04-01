"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc

from app.basestate import BaseState


class AuthState(BaseState):
    user: str = ""
    pwd: str = ""

    def set_pwd(self, text):
        self.pwd = text

    def set_user(self, text):
        self.user = text

    def set_client(self):
        print("SETTING CLIENT")
        self.admin = False

    def set_admin(self):
        print("SETTING ADMIN")
        self.admin = True

    def login(self):
        if self.user.lower() == "admin" and self.pwd.lower() == "admin":
            self.set_admin()
        else:
            with pc.session() as session:
                result = session.execute("SELECT * FROM customer")
                # TODO: finish up
                self.set_client()


def index():
    return pc.center(
        pc.vstack(
            pc.heading("E-Hotel Service", font_size="2em"),
            pc.box("by Mershab Issadien"),
            pc.box("Login",
                   pc.input(
                       placeholder="Username",
                       on_blur=AuthState.set_user,
                   ),
                   pc.input(
                       placeholder="Password",
                       on_blur=AuthState.set_pwd,
                   ),
                   pc.link(
                       pc.button(
                           "Login",
                           border_radius="1em",
                           box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                           background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                           box_sizing="border-box",
                           color="white",
                           on_click=lambda: AuthState.login,
                           _hover={
                               "opacity": 0.85,
                           },
                       ),
                       href="/landing",
                       color="rgb(107,99,246)",
                       button=True,
                   ),
                   spacing="1.5em",
                   font_size="2em",
                   )
        ),
        padding_top="10%",
    )
