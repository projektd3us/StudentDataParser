from openpyxl import load_workbook


def cellToInt(cell):
    """
    Converts a cell from a xlsx file to a int value

    :param cell cell: excel cell

    :rtype: int
    :return: converted value from cell

    :raises TypeError if not int inside cell
    """
    try:
        return int(str(cell)[1:]) - 9
    except:
        raise TypeError


def xlsxParse(fileName):
    """
    Parses an xlsx file in order to return its last cell. Value used in counting students.

    :param str fileName : file name to be parsed

    :rtype: cell
    :return: last cell from file
    """
    wb = load_workbook(fileName)
    wCells = wb['Sheet1']
    lastCell = 'A100'  # presumed end
    for count, i in enumerate(wCells['A9':lastCell]):  # first stud name to presumed end cell
        cellName = 'A' + str(count + 9)  # current cell name
        if not wCells[cellName].value:
            lastCell = cellName
            break  # found last cell, then fuck off
    return lastCell
