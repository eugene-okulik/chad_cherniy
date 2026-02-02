from datetime import datetime
from typing import Optional

class Flowers:
    def __init__(
            self,
            name: str,
            price: float,
            stem_length: float,  # длина стебля в см
            month_of_maturation: str,  # месяц созревания
            color: str = "неизвестный"
    ):

        self.name = name
        self.price = price
        self.stem_length = stem_length
        self.month_of_maturation = month_of_maturation
        self.color = color

        def __str__() -> str:
            return (f"{self.name} ({self.color}), цена: {self.price}₽, "
                    f"стебель: {self.stem_length}см, месяц созревания: {self.month_of_maturation}.")


class Roza(Flowers):
    def __init__(
            self,
            price: float,
            stem_length: float,
            month_of_maturation: str,
            color: str = "красный",
            has_thorns: bool = True,
            variety: str = "чайно-гибридная"
    ):
        super().__init__("Роза", price, stem_length, month_of_maturation, color)
        self.has_thorns = has_thorns # шипы
        self.variety = variety  # сорт розы

    def __str__(self) -> str:
        thorns_info = "с шипами" if self.has_thorns else "без шипов"
        return f"{super().__str__()}, {thorns_info}, сорт: {self.variety}"


class Tulpan(Flowers):
    def __init__(
            self,
            price: float,
            stem_length: float,
            month_of_maturation: str,
            color: str = "жёлтый",
            bud_size: str = "средний"  # маленький, средний, крупный
    ):
        super().__init__("Тюльпан", price, stem_length, month_of_maturation, color)
        self.bud_size = bud_size

    def __str__(self) -> str:
        return f"{super().__str__()}, бутон: {self.bud_size}"


class Hrizantema(Flowers):
    def __init__(
            self,
            price: float,
            stem_length: float,
            month_of_maturation: str,
            color: str = "белый",
            inflorescence_type: str = "помпонный"  # помпонный, анемоновидный, плоский
    ):
        super().__init__("Хризантема", price, stem_length, month_of_maturation, color)
        self.inflorescence_type = inflorescence_type    # Тип соцветия

    def __str__(self) -> str:
        return f"{super().__str__()}, тип соцветия: {self.inflorescence_type}."


# Экземпляры разных цветов
rosa1 = Roza(price=150.0, stem_length=60, month_of_maturation='July', color="бордовый", variety="Пионовидная")
tulpan1 = Tulpan(price=80.0, stem_length=40, month_of_maturation='March', color="оранжевый", bud_size="крупный")
hrizantema1 = Hrizantema(price=120.0, stem_length=50, month_of_maturation='June', color="жёлтый",
                         inflorescence_type="анемоновидный")
