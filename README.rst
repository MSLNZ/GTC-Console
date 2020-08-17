===========================
GUM Tree Calculator Console 
===========================

This project produces a stand-alone Windows executable for the GUM Tree Calculator, which can be used without the need to have Python installed on the host computer. 

Background
==========

MSL first made GUM Tree Calculator available as a stand-alone Windows executable and called it "GTC". Later, we released GTC as an open-source Python package, and the Windows executable version became known as "GTC Console". 
The two versions have different code bases; GTC Console code was only compatible with Python 2.x, whereas the newer GTC code would run on Python 2.7 and 3.x.

GTC Console was produced using a tool called "py2exe", which is no longer actively supported and doesn't work with more recent versions of Python. So, this project intends to reproduce GTC Console using the new GTC (Python) code base and a different tool, called "Pyinstaller". The change in code base means there will not be full code-compatibility between this tool and earlier versions of GTC console, however the changes to the API have been relatively minor. 
 
Status
======

This is a new project. 

The initial goal is to create a stand-alone Windows executable with roughly equivalent functionality to the previous GTC Console. There will not be full code compatibility with previous versions, because the code base has changed. 





