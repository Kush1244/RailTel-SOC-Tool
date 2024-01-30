import tkinter.messagebox as mbox
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *


def make_table(col_name, row_name):
    app = ttk.Window()
    colors = app.style.colors
    dt = Tableview(
        master=app,
        coldata=col_name,
        rowdata=row_name,
        paginated=False,
        searchable=True,
        bootstyle=SUCCESS,
        stripecolor=("lightgreen", None),
    )
    dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    app.mainloop()
