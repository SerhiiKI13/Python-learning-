from openpyxl.worksheet.filters import Filters,FilterColumn
from openpyxl.worksheet.table import Table, TableStyleInfo

filters = Filters(filter=["Torun"])

filter_column = FilterColumn(
    colId= 2,
    filters=filters
)
