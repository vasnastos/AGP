import xlsxwriter
import csv,os
from pick import pick

class InputF:
    @staticmethod
    def get_temp_data():
        files=os.listdir(os.path.join('','Source'))
        return {fn:os.path.join('','Source',fn) for fn in files}

def convert_csv_to_excel():
    samples=InputF.get_temp_data()
    fn=selected_file.replace('.csv','')
    writer=xlsxwriter.Workbook(fn+'.xlsx')
    sheet=writer.add_worksheet()
    row=0
    selected_file,_=pick(options=list(samples.keys()),title="Select File")
    file_input=InputF.options[selected_file]
    with open(file_input,'r') as RF:
        csv_reader=csv.reader(RF)
        for drow in csv_reader:
            for index,value in enumerate(list(drow)):
                sheet.write(row,index,value)
            row+=1
    writer.close()


if __name__=='__main__':
    convert_csv_to_excel()
