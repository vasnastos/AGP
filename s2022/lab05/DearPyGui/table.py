import dearpygui.dearpygui as dpg
import csv,os

class Window:
    def __init__(self,w,h):
        self.window_width=w
        self.window_height=h
        dpg.create_context()
        dpg.create_viewport(title='Table demo',width=w,height=h)

        with dpg.window(label='Table Demo',width=w*0.97,height=h*0.9):
            with dpg.table(header_row=False,resizable=True,policy=dpg.mvTable_SizingStretchProp,borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True):
                dpg.add_table_column(label="Name")
                dpg.add_table_column(label="Team")
                dpg.add_table_column(label="Position")
                dpg.add_table_column(label="Height")
                dpg.add_table_column(label="Weight")
                dpg.add_table_column(label="Age")
            
                with open(os.path.join('..','Source','mlb_players.csv'),'r') as RF:
                    csv_reader=csv.reader(RF)
                    for x in csv_reader:
                        with dpg.table_row():
                            for val in x:
                                with dpg.table_cell():
                                    dpg.add_text(val)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()



if __name__=='__main__':
    w=Window(600,600)
