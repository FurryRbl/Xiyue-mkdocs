import re
import json
from types import SimpleNamespace


def on_page_markdown(markdown, **kwargs):
    ### 含高级选项的图片 ###
    def imageHaveSize(match):
        optionDefault = {"width": "30%", "height": "30%"}
        title = match.group(1)  ### 标题 ###
        url = match.group(2)  ### 图片地址 ###
        option = json.loads("{" + match.group(3) + "}")
        option = SimpleNamespace(**{**optionDefault, **option})  ### 高级选项 ###
        del optionDefault
        html = f"""
<div class="images">
    <img href="{url}" data-fancybox="gallery" data-caption="{title}" src="{url}" width="{option.width}" height="{option.height}" alt="图片无法加载！"/>
    <p>{title}</p>
</div>
        """
        return html

    ### 正常图片，高级图片后解析 ###
    def image(match):
        title = match.group(1)  ### 标题 ###
        url = match.group(2)  ### 图片地址 ###
        html = f"""
<div class="images">
    <img href="{url}"data-fancybox="gallery" data-caption="{title}" src="{url}" width="30%" height="30%" alt="图片无法加载！"/>
    <p>{title}</p>
</div>
        """
        return html

    ### 图片 ###
    markdown = re.sub(
        r"!\[(.*?)\]\((.*?)\)\s*\{([^}]+)\}", imageHaveSize, markdown
    )  # 含高级选项的图片
    markdown = re.sub(r"!\[(.*?)\]\((.*?)\)", image, markdown)  # 默认图片

    return markdown
