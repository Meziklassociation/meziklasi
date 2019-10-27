class Spoiler < Liquid::Tag
  def initialize(tag_name, input, tokens)
    super
    @input = input
  end

  def render(context)
	output = "<blockquote class='spoiler'>"
	output += @input
	output += "</blockquote>"

    return  output;
  end

end
Liquid::Template.register_tag('spo', Spoiler)
