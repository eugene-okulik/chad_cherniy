from typing import List

class Flowers:

    # Максимальный срок жизни после срезки (в днях) для базового класса
    MAX_LIFE_DAYS = 7

    def __init__(
            self,
            name: str,
            price: float,
            stem_length: float,  # длина стебля в см
            freshness_days: int,  # дней с момента срезки
            month_of_maturation: str,  # месяц созревания
            color: str = "неизвестный"
    ):

        self.name = name
        self.price = price
        self.stem_length = stem_length
        self.freshness_days = freshness_days  # свежесть: сколько дней прошло с момента срезки
        self.month_of_maturation = month_of_maturation
        self.color = color

    def remaining_life(self) -> int:
        # Оставшийся срок жизни цветка в днях.
        return max(0, self.MAX_LIFE_DAYS - self.freshness_days)

    def __str__(self) -> str:
        return (f"{self.name} ({self.color}), цена: {self.price}₽, "
                f"стебель: {self.stem_length}см, свежесть: {self.freshness_days}дн., "
                f"осталось жизни: {self.remaining_life()}дн."
                f", месяц созревания: {self.month_of_maturation}.")


class Roza(Flowers):
    MAX_LIFE_DAYS = 10

    def __init__(
        self,
        price: float,
        stem_length: float,
        freshness_days: int,
        month_of_maturation: str = "Июнь",
        color: str = "красный",
        variety: str = "чайно-гибридная"  # уникальный атрибут розы
    ):
        super().__init__(
            "Роза",
            price,
            stem_length,
            freshness_days,
            month_of_maturation,
            color
        )
        self.variety = variety  # сорт

    def __str__(self) -> str:
        return f"{super().__str__()}, сорт: {self.variety}"


class Tulpan(Flowers):
    """Класс для тюльпанов."""
    MAX_LIFE_DAYS = 5

    def __init__(
        self,
        price: float,
        stem_length: float,
        freshness_days: int,
        month_of_maturation: str = "Апрель",
        color: str = "жёлтый",
        bud_size: str = "средний"  # уникальный атрибут тюльпана
    ):
        super().__init__(
            "Тюльпан",
            price,
            stem_length,
            freshness_days,
            month_of_maturation,
            color
        )
        self.bud_size = bud_size    # Размер бутона

    def __str__(self) -> str:
        return f"{super().__str__()}, размер бутона: {self.bud_size}"


class Hrizantema(Flowers):
    """Класс для хризантем."""
    MAX_LIFE_DAYS = 14

    def __init__(
        self,
        price: float,
        stem_length: float,
        freshness_days: int,
        month_of_maturation: str = "Сентябрь",
        color: str = "белый",
        inflorescence_type: str = "помпонный"  # уникальный атрибут хризантемы
    ):
        super().__init__(
            "Хризантема",
            price,
            stem_length,
            freshness_days,
            month_of_maturation,
            color
        )
        self.inflorescence_type = inflorescence_type    # Тип соцветия

    def __str__(self) -> str:
        return f"{super().__str__()}, тип соцветия: {self.inflorescence_type}"


# Экземпляры разных цветов
rosa1 = Roza(price=150.0, stem_length=60, freshness_days=2, month_of_maturation='Июль', color="бордовый")
rosa2 = Roza(price=140.0, stem_length=50, freshness_days=1, month_of_maturation='Июнь', color="красный")
tulpan1 = Tulpan(price=80.0, stem_length=40, freshness_days=1, month_of_maturation='Март', color="оранжевый")
tulpan2 = Tulpan(price=70.0, stem_length=35, freshness_days=2, month_of_maturation='апрель', color="желтый")
hrizantema1 = Hrizantema(price=120.0, stem_length=50, freshness_days=2, month_of_maturation='Июнь', color="жёлтый")
hrizantema2 = Hrizantema(price=100.0, stem_length=40, freshness_days=3, month_of_maturation='Май', color="белый")


class Buket:
    def __init__(self, name: str = "Букет"):
        self.name = name
        self.flowers: List[Flowers] = []  # Список объектов цветов

