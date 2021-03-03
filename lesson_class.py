"""
Класс "изделие"(Product), который записывает атрибуты введенные пользователем в БД.
Класс "калькуляция"(Offer), который берёт данные из БД, и с помощью методов выдаёт значение стоимости, 
добавляет её в ту же БД.
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
        self.weight = weight # масса детали
        self.rate = rate # н.р. материала +25%
        self.coating = coating #coating - список
        self.labour = labour #покрытие +10%
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
