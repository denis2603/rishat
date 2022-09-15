from django.core.management import BaseCommand
from ...models import Item
import random


class Command(BaseCommand):
    help = 'Добавление в базу данных тестовых товаров'
    item_count = 10  # количество добавленных магазинов

    def handle(self, *args, **options):
        for i in range(self.item_count):
            item = Item(
                name=f'Item {i + 1}',
                description=f'Description of item {i + 1}',
                price=random.randint(1, int(1e6)) / 100,
            )
            item.save()

        return f'Товары успешно добавлены, {self.item_count} шт.'
