wxpython环境搭建及编程

windows下搭建wxPython环境
Mac下搭建wxpython环境
新技能：可视化编程实现

准备工作
windows下安装wxpython

如何确定python的位数？
python可以直接查看

wxpython的安装：
1.
next

什么是可视化编程
可视化编程常用工具
可视化编程的实现

什么是可视化编程？
在GUI编程中，我们可以通过写代码的方式来创建相应的图形界面，同样，也可以直接使用图形界面可视化开发出图形界面
对于后者，相对来说开发难度小得多。

可视化编程
代码编程

可视化编程工具：
wxFormBuilder
wxDesigner, gui2py,

简单的窗口

# !/usr/bin/env python
# coding: utf8
# author: youdi



###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class XbFrame1
###########################################################################

class XbFrame1(wx.Frame):
    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"我的窗口", pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"友弟", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(15, 75, 90, 90, False, "黑体"))
        self.m_staticText1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        bSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == '__main__':
    app = wx.App()
    f1 = XbFrame1(None)
    f1.Show()
    app.MainLoop()

菜单：

# !/usr/bin/env python
# coding: utf8
# author: youdi


# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.dataview
import wx.animate


###########################################################################
## Class XbFrame1
###########################################################################

class XbFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"GUI", pos=wx.DefaultPosition, size=wx.Size(767, 495),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"友弟", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(15, 75, 90, 90, False, "黑体"))
        self.m_staticText1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        bSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_treeCtrl1 = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)
        gbSizer1.Add(self.m_treeCtrl1, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_grid2 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid2.CreateGrid(5, 5)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(0, 0)

        # Columns
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelSize(30)
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelSize(80)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gbSizer1.Add(self.m_grid2, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        m_checkList1Choices = []
        self.m_checkList1 = wx.CheckListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList1Choices, 0)
        gbSizer1.Add(self.m_checkList1, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_dataViewCtrl1 = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_dataViewCtrl1, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_dataViewListCtrl1, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_button1, wx.GBPosition(0, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.m_button2, wx.GBPosition(0, 6), wx.GBSpan(1, 1), wx.ALL, 5)

        bSizer1.Add(gbSizer1, 1, wx.EXPAND, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_bpButton1 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        bSizer1.Add(self.m_bpButton1, 0, wx.ALL, 5)

        self.m_bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_bitmap1, 0, wx.ALL, 5)

        self.m_animCtrl1 = wx.animate.AnimationCtrl(self, wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition,
                                                    wx.DefaultSize, wx.animate.AC_DEFAULT_STYLE)
        bSizer1.Add(self.m_animCtrl1, 0, wx.ALL, 5)

        m_listBox1Choices = []
        self.m_listBox1 = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0)
        bSizer1.Add(self.m_listBox1, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menu11 = wx.Menu()
        self.m_menuItem2 = wx.MenuItem(self.m_menu11, wx.ID_ANY, u"project", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu11.AppendItem(self.m_menuItem2)

        self.m_menuItem3 = wx.MenuItem(self.m_menu11, wx.ID_ANY, u"file", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu11.AppendItem(self.m_menuItem3)

        self.m_menu1.AppendSubMenu(self.m_menu11, u"new File")

        self.m_menu21 = wx.Menu()
        self.m_menu1.AppendSubMenu(self.m_menu21, u"open")

        self.m_menu31 = wx.Menu()
        self.m_menu1.AppendSubMenu(self.m_menu31, u"save")

        self.m_menu41 = wx.Menu()
        self.m_menu1.AppendSubMenu(self.m_menu41, u"Exit")

        self.m_menuItem1 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Import", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.AppendItem(self.m_menuItem1)

        self.m_menubar1.Append(self.m_menu1, u"File")

        self.m_menu2 = wx.Menu()
        self.m_menu51 = wx.Menu()
        self.m_menu2.AppendSubMenu(self.m_menu51, u"undo")

        self.m_menu6 = wx.Menu()
        self.m_menu2.AppendSubMenu(self.m_menu6, u"redo")

        self.m_menubar1.Append(self.m_menu2, u"Edit")

        self.m_menu3 = wx.Menu()
        self.m_menubar1.Append(self.m_menu3, u"View")

        self.m_menu4 = wx.Menu()
        self.m_menubar1.Append(self.m_menu4, u"Tools")

        self.m_menu5 = wx.Menu()
        self.m_menubar1.Append(self.m_menu5, u"Help")

        self.SetMenuBar(self.m_menubar1)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == '__main__':
    app = wx.App()
    f1 = XbFrame1(None)
    f1.Show()
    app.MainLoop()

wxpython介绍
wxpython是wxWidgets在python语言下的封装
wxWidgets是一个跨平台的GUI应用程序编程接口，使用C + +编写的。
所想即所得，缺乏成熟的IDE
图形界面风格与系统的风格相似

为什么选择wxPython而不是pyQt？
协议：封闭
编码风格
复杂性
个人习惯

基本空间介绍
绝对布局

基本控件：
静态文本：wx.StaticText
文本域：wx.TextCtrl
按钮：wx.Button
单选框与复选框：wx.CheckBox / wx.RadioBox
列表框： wx.ListBox
图片：wx.Image

绝对布局
基于控件的坐标摆放控件
简单直观
方法单一
不能随窗口的改变而调整位置

button = wx.Bottom(parent=panel, label=u'这是按钮', pos=(50, 50))
其中位置
pos = (1, 2)
size, 大小

# !/usr/bin/env python
# coding: utf8
# author: youdi

import wx


# app = wx.App()
# frame = wx.Frame(None, -1, u'GUI学习')
# frame.Show()
# app.MainLoop()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, id=-1, title=u'GUI学习', size=(600, 600))
        panel = wx.Panel(self, -1)
        self.Centre()

        button = wx.Button(panel, id=-1, label=u'这是按钮', pos=(50, 50))
        statictext = wx.StaticText(parent=panel, id=-1, label=u'这是静态文本框', pos=(20, 100))
        text = wx.TextCtrl(panel, -1, u'这是文本', pos=(200, 210))
        password = wx.TextCtrl(panel, -1, u'输入密码', style=wx.TE_PASSWORD, pos=(200, 250))
        mutiText = wx.TextCtrl(panel, -1, u'请输入多行内容', style=wx.TE_MULTILINE, pos=(100, 300))
        checkBox1 = wx.CheckBox(panel, -1, u'这是复选框1', pos=(150, 20))
        checkBox2 = wx.CheckBox(panel, -1, u'这是复选框1', pos=(150, 40))

        radio1 = wx.RadioButton(panel, -1, u'这是单选框1', pos=(150, 60), style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, -1, u'这是单选框2', pos=(150, 60))
        radio3 = wx.RadioButton(panel, -1, u'这是单选框3', pos=(150, 60))

        radiolist = [u'一组单选按钮1', u'一组单选按钮2', u'一组单选按钮3']
        wx.RadioBox(panel, -1, u'一组单选按钮', (10, 120), wx.DefaultSize, radiolist, 2, wx.RA_SPECIFY_COLS)

        tuxinghua = [u'图', u'形', u'化', u'篇', '1', '2', '3', '4', '5', '6']
        listbox = wx.ListBox(panel, -1, pos=(300, 20), size=(100, 100), choices=tuxinghua, style=wx.LB_SINGLE)

        img = wx.Image(r'../img/5.jpg', wx.BITMAP_TYPE_ANY).Scale(200, 200)
        sb1 = wx.StaticBitmap(panel, -1, wx.BitmapFromImage(img), pos=(300, 300))


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

控件相对布局：
    BoxSizer管理布局
    GridSize管理布局
    FlexGridSize管理布局
    GridBagSize管理布局

BoxSizer管理布局
    一行一列，可以选择行扩展或者列扩展

GridSize管理布局
    多行多列，每一格大小相等

FlexGridSizer管理布局
    多行多列，同一行高度相等，同一列宽度相等

GridBagSizer管理布局
    多行多列，每个单元格均能长宽随意，还可以跨行跨列

多线程与事件

python多线程
    不使用多线程可能会导致图形界面卡死
    多线程可以使程序以更高的效率运行
    多线程可以让程序做更多事情
    thread.start_new_thread(函数名，(参数1，参数2))
    使用threading模块创建线程

控件的事件：
    按钮点击
    文本域内容的改变
    鼠标滑过
    鼠标双击
    键盘按下
    ....


python编写图形界面的程序
能与程序上面的控件进行交互
程序不会卡死
程序控件的布局不会因为界面的大小改变而混乱




wx

import wx
# 每个wxPython的程序必须有一个wx.App对象
app = wx.App()  # default is False,当为Ture的时候，错误和输出都输出到窗口，false输出到控制台

frame = wx.Frame(None,-1,title="hello,World",pos=(300,400),size=(200,150))
# frame.Centre()
frame.Show()

# 进入循环，等待响应
app.Main()

