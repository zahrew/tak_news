from tak_news.news.models import News, Tag


class NewsScraperPipeline:

    def process_item(self, item, spider):
       
        tags = []
        for tag_name in item.get('tags', []):
            tag, created = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)

        
        news, created = News.objects.get_or_create(
            title=item.get('title'),
            defaults={'content': item.get('content'), 'source': item.get('source')}
        )

        news.tags.set(tags)
        news.save()

        return item
