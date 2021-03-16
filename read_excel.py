import xlrd

def load_data(excel_file):
    wb = xlrd.open_workbook(excel_file)
    table = wb.sheet_by_index(0)
    nNum = table.nrows
    data = []
    for i in range(nNum):
        data.append(table.row_values(i))
    return data

if __name__ == "__main__":
    print(load_data(r'data_list\小品节目单.xlsx'))