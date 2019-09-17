module Jekyll
  class PermalinkRewriter < Generator
    safe true
    priority :low
    
    def generate(site)
      # see https://stackoverflow.com/questions/31416559/i18ninvalidlocale-en-is-not-a-valid-locale
      I18n.config.available_locales = :en
      
      # change each of the permalinks
      site.posts.docs.each do |item|
        category = I18n.transliterate(item.data['category'].downcase.gsub(" ", "-"))
        title = item.data['slug']

        item.data['permalink'] = "#{category}/#{title}/"
      end
    end
  end
end
