"""
В качестве ссылки на репоз. составить 3 различных класса:
- объект любой, метод инит, в котором от 3х до 5ти атрибутов
- для конструктора - в кач. аргумента
- аннотация типов, документация, описание тех параметра.
- написать 3-5 методов, которые будут реализовывать работу объекта
"""


class Product:

"""
1ый класс - изделие, которое необходио изготовить. 
Атрибуты - наименование, номер, материал, масса, н.р. материала, наличие покрытия, трудоёмкость, операции при изготовлении
Методы - увеличение трудоёмкости на 10% при наличии покрытия;
       - н.р. = +25% к массе
       - отметка об изготовлении
       - маршрут изготовления по цехам
"""

    def __init__(self, name: str, decimal: str, material:str, weight: float, rate: float, coating: bool, labour: int, operation):

        self.name = name
        self.decimal = decimal
        self.material = material #material - список
        self.weight = weight
        self.rate = rate
        self.coating = coating #coating - список
        self.labour = labour
        self.operation = operation #operation - словарь (ключ - название, значение - код)

    def consumption_rate(rate):
        """
        Расчет н.р. материала
        """
        return rate*1.25


    def coating_met(labour, coating):
        """
        Проверка на наличие покрытия
        :param coating:
        :return:
        """
        if coating:
            return labour*1.1


    def operations_route(operation):
        """
        Маршрут изготовления
        Вывести пользователю список операций с кодами,
        присвоить объету сет с выбранными операциями
        :param operation:
        :return:
        """


        ...


    def complete_product(labour):
        """
        Отметка об изготовлении.
        Ставится "Выполнено", когда текущая дата = дата старта + трудоёмкость
        """
