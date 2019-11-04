Jekyll::Hooks.register :posts, :post_render do |post|
	post_data = post.to_s();
	post_data.gsub(/\€(.{1,32})\€/, '\<div class="spoiler"\> \1 \<div\>')
end
