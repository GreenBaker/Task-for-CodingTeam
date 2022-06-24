import django
from Foods.models import Food, FoodCategory
django.setup()


def setUpFoodsCategory():
        FoodCategory.objects.create(name_ru="Напитки(some items is_publish=True)")
        FoodCategory.objects.create(name_ru="Выпечка(all items is_publish=False)")
        FoodCategory.objects.create(name_ru="Мороженое(all items is_publish=True")
        FoodCategory.objects.create(name_ru="Веган(empty category)")


def setUpDrinks():

        Food.objects.create(
            internal_code=100,
            code=1,
            name_ru="Чай",
            category_id=1,
            description_ru="Чай 100 гр",
            cost=120.00,
            is_publish=True,
        )

        Food.objects.create(
            internal_code=200,
            code=2,
            name_ru="Кола",
            category_id=1,
            description_ru="Кола",
            cost=123.50,
            is_publish=True,
        )

        Food.objects.create(
            internal_code=300,
            code=3,
            name_ru="Спрайт",
            category_id=1,
            description_ru="Спрайт",
            cost=100.50,
            is_publish=True,
        )

        Food.objects.create(
            internal_code=400,
            code=4,
            name_ru="Байкал(is_publish=False)",
            category_id=1,
            description_ru="Байкал",
            cost=20.50,
            is_publish=False,
        )


def setUpOtherFood():

        Food.objects.create(
            internal_code=110,
            code=11,
            name_ru="Булка",
            category_id=2,
            description_ru="Булка",
            cost=10.00,
            is_publish=False,
        )

        Food.objects.create(
            internal_code=120,
            code=12,
            name_ru="Рогалик",
            category_id=2,
            description_ru="Рогалик",
            cost=6.66,
            is_publish=False,
        )

        Food.objects.create(
            internal_code=130,
            code=13,
            name_ru="Фисташковое мороженое",
            category_id=3,
            description_ru="Фисташковое мороженое",
            cost=10.50,
            is_publish=True,
        )

        Food.objects.create(
            internal_code=140,
            code=14,
            name_ru="Шоколадное мороженое",
            category_id=3,
            description_ru="Шоколадное мороженое",
            cost=11.50,
            is_publish=True,
        )


setUpFoodsCategory()
setUpDrinks()
setUpOtherFood()
