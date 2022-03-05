from cProfile import label
import dearpygui.dearpygui as dpg

def popout_message_box(sender,unused,user_data):
    dpg.delete_item(user_data[0])

def show_info(title, message):
    # guarantee these commands happen in the same frame
    with dpg.mutex():

        viewport_width = dpg.get_viewport_client_width()
        viewport_height = dpg.get_viewport_client_height()

        with dpg.window(label=title, modal=True, no_close=True) as modal_id:
            dpg.add_text(message)
            dpg.add_button(label="Ok", width=75, user_data=(modal_id, True),callback=popout_message_box)

    # guarantee these commands happen in another frame
    dpg.split_frame()
    width = dpg.get_item_width(modal_id)
    height = dpg.get_item_height(modal_id)
    dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])



class Window:
    def __init__(self,w,h):
        self.width,self.height=w,h
        dpg.create_context()
        with dpg.window(label="Radio Button",width=self.width,height=self.height):
            self.rad_handling=dpg.add_radio_button(items=['Item 1','Item 2','Item 3'],horizontal=False)
            dpg.add_button(label="CHECK",callback=self.button_action)
        dpg.create_viewport(title='Radio Button',width=w,height=h)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
    
    def button_action(self):
        show_info("Radio Button Selection","You selected {}".format(dpg.get_value(self.rad_handling)))


if __name__=='__main__':
    w=Window(600,600)