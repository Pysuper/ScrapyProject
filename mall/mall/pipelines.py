class MallPipeline(object):
    def process_item(self, item, spider):
        print(dict(item))
        return item
