===========================
GUM Tree Calculator Console 
===========================

This project produces a stand-alone Windows executable for GTC, which can be distributed and used without the need to have Python installed on the host computer. 

Background
==========

MSL first made GUM Tree Calculator available as a Windows executable and called it GTC. This tool was distributed with the SciTE editor to help development. 

Then later MSL released a public Python package for GTC, and so we began to call the Windows executable version "GTC Console". They did not use the same code. 

The Python tool used to produce the original GTC Console (py2exe) doesn't work with recent versions of Python. So, this project is will generate GTC Console with different tools, using the GTC (Python) code base.
 
Status
======

This GTC Console is just starting out. The first goal is to create a stand-alone Windows executable for Windows machines. After this has been achieved, we will look at providing documentation and an installer.



