import dearpygui.dearpygui as dpg

class Window:
    def __init__(self,w,h):
        self.width,self.height=w,h
        self.tasks=[]
        dpg.create_context()
        dpg.create_viewport(title='TODO LIST',width=w,height=h)
        with dpg.window(label='TODO LIST',width=w,height=h):
            with dpg.group(label='Group 1',horizontal=True):
                self.task=dpg.add_input_text(default_value='todo object list')
                dpg.add_button(label='ADD',callback=self.add_task)
            dpg.add_spacer(height=0.2)
            self.todo_obj=dpg.add_listbox(items=self.tasks,width=0.96*self.width)
    
    def add_task(self):
        task=dpg.get_value(self.task)
        self.tasks.append(task)
        dpg.add_ite

    def show(self):
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()


if __name__=='__main__':
    w=Window(600,600)
    w.show()