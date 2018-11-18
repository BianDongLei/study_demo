from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.pdfdevice import PDFDevice

# 获取需要读取的PDF文档对象
pdfFile = open("一种折叠屏上使用的付款码使用方式.pdf", "rb")
# 创建PDF解释器
pdfParser = PDFParser(pdfFile)
# 创建PDFDocument对象
pdfDoc = PDFDocument()
# 链接解释器和PDFDocument对象
pdfParser.set_document(pdfDoc)
pdfDoc.set_parser(pdfParser)
# 初始化文档，这里传入参数为PDF文档的密码
pdfDoc.initialize("")
# 创建PDF的资源管理器和参数分析器
pdfRes = PDFResourceManager()
pdfLaparams = LAParams()
# 创建聚合器和页面解释器
pdfDevice = PDFPageAggregator(pdfRes,laparams=pdfLaparams)
pdfInte = PDFPageInterpreter(pdfRes,pdfDevice)

for page in pdfDoc.get_pages():
    pdfInte.process_page(page)
    for out in pdfDevice.get_result():
        if hasattr(out,"get_text"):
            print(out.get_text())
#
# for (level,title,dest,a,se) in pdfDoc.get_outlines():
#     print(level,title,dest,a,se)

