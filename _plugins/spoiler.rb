class Spoiler < Liquid::Tag
  def initialize(tag_name, input, tokens)
    super
    @input = input
  end

  def render(context)
	output = "<div><div class='spoiler'>" + @input + "</div></div>" 
	
    return  output;
  end

end
Liquid::Template.register_tag('spoiler', Spoiler)
