import dearpygui.dearpygui as dpg

class Window:
    def __init__(self,width=600,height=600):
        dpg.create_context()
        dpg.create_viewport(title='First App',width=width,height=height)
        with dpg.window(label='Login Form',width=width,height=height):
            self.username=dpg.add_input_text(default_value='Username')
            self.password=dpg.add_input_text(default_value='Password')
            dpg.add_button(label="Login",callback=self.login_screen)
            dpg.add_same_line()
            dpg.add_button(label='Clear',callback=self.clear_input)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()


    def login_screen(self):
        print("Login Username:{}".format(dpg.get_value(self.username)))
        print("Login Password:{}".format(dpg.get_value(self.password)))

    def clear_input(self):
        dpg.set_value(self.username,'')
        dpg.set_value(self.password,'')

if __name__=='__main__':
    w=Window()

    