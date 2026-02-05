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


class Buket:
    def __init__(self, name: str = "Букет"):
        self.name = name
        self.flowers: List[Flowers] = []  # Список объектов цветов

    def add_flower(self, flower: Flowers) -> None:
        # Добавляем один цветок
        self.flowers.append(flower)

    def add_flowers(self, *flowers: Flowers) -> None:
        # Добавить несколько цветов
        self.flowers.extend(flowers)

    def total_price(self) -> float:
        # Рассчитываем общую стоимость букета на основе цен цветов
        return sum(flower.price for flower in self.flowers)

    def time_of_live(self) -> float:    # Определяем время жизни
        if not self.flowers:
            return 0.0
        total_remaining = sum(flower.remaining_life() for flower in self.flowers)
        return total_remaining / len(self.flowers)

    def sort_by(self, param: str, reverse: bool = False) -> None:
        """
        Доступные параметры:
            'freshness' - по свежести (дни с момента срезки)
            'color' - по цвету
            'stem_length' - по длине стебля
            'price' - по стоимости
        """
        sort_keys = {
            'freshness': lambda f: f.freshness_days,
            'color': lambda f: f.color.lower(),
            'stem_length': lambda f: f.stem_length,
            'price': lambda f: f.price,
        }

        if param not in sort_keys:
            raise ValueError(
                f"Недопустимый параметр: '{param}'. "
                f"Доступные: {', '.join(sort_keys.keys())}"
            )

        self.flowers.sort(key=sort_keys[param], reverse=reverse)

    def find_by(self, **criteria) -> List[Flowers]:

        results = self.flowers[:]

        if 'min_remaining_life' in criteria:
            results = [f for f in results if f.remaining_life() >= criteria['min_remaining_life']]

        if 'max_remaining_life' in criteria:
            results = [f for f in results if f.remaining_life() <= criteria['max_remaining_life']]

        if 'color' in criteria:
            color = criteria['color'].lower()
            results = [f for f in results if color in f.color.lower()]

        return results


if __name__ == "__main__":
    # Создаём экземпляры цветов разных видов
    roza1 = Roza(
        price=150.0,
        stem_length=60,
        freshness_days=2,
        month_of_maturation="Июль",
        color="бордовый",
        variety="Пионовидная"
    )

    roza2 = Roza(
        price=140.0,
        stem_length=55,
        freshness_days=1,
        month_of_maturation="Июнь",
        color="красный",
        variety="Экватор"
    )

    tulpan1 = Tulpan(
        price=80.0,
        stem_length=40,
        freshness_days=1,
        month_of_maturation="Март",
        color="оранжевый",
        bud_size="крупный"
    )

    tulpan2 = Tulpan(
        price=75.0,
        stem_length=38,
        freshness_days=2,
        month_of_maturation="Апрель",
        color="жёлтый",
        bud_size="средний"
    )

    hrizantema1 = Hrizantema(
        price=120.0,
        stem_length=50,
        freshness_days=3,
        month_of_maturation="Сентябрь",
        color="жёлтый",
        inflorescence_type="анемоновидный"
    )

    hrizantema2 = Hrizantema(
        price=110.0,
        stem_length=48,
        freshness_days=2,
        month_of_maturation="Октябрь",
        color="белый",
        inflorescence_type="помпонный"
    )

    # Создаём букет и добавляем цветы
    buket = Buket("Фортиус букет")
    buket.add_flowers(roza1, tulpan1, hrizantema1, roza2, tulpan2, hrizantema2)

    # Сортировка по разным параметрам
    print("\n🌸 Сортировка по свежести (самые свежие первыми):")
    buket.sort_by('freshness')
    for f in buket.flowers:
        print(f"  {f.name}: {f.freshness_days}дн.")

    # Поиск цветов по критериям
    print("\n🔍 Поиск цветов с оставшимся сроком жизни >= 8 дней:")
    long_living = buket.find_by(min_remaining_life=8)
    if long_living:
        for f in long_living:
            print(f"  {f}")
    else:
        print("  Не найдено")

    print("\n🔍 Поиск жёлтых цветов:")
    yellow_flowers = buket.find_by(color="жёлтый")
    for f in yellow_flowers:
        print(f"  {f}")

    # Финальная информация
    print("\n" + "=" * 80)
    print(f"Название букета: {buket.name}")
    print(f"Количество цветов: {len(buket.flowers)}")
    print(f"Общая стоимость: {buket.total_price():.2f}₽")
    print(f"Среднее время до увядания: {buket.time_of_live():.1f} дней")
    print("=" * 80)
