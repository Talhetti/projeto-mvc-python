class ItemController:
    def __init__(self, item_model):
        self.item_model = item_model

    def create_item(self, name, description):
        new_item = self.item_model(name=name, description=description)
        new_item.save()
        return new_item

    def get_all_items(self):
        return self.item_model.query.all()

    def get_item(self, item_id):
        return self.item_model.query.get(item_id)

    def update_item(self, item_id, name, description):
        item = self.get_item(item_id)
        if item:
            item.name = name
            item.description = description
            item.save()
        return item

    def delete_item(self, item_id):
        item = self.get_item(item_id)
        if item:
            item.delete()
        return item