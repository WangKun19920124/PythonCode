# 调用GitHub的WebAPI获取数据
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("status code = ", r.status_code)  # 状态码

response_dict = r.json()    # 返回结果（字典）
print("total repositories = ", response_dict['total_count'])    # 所有仓库数

repos = response_dict['items'] # 返回字典的列表
print('returned repositories = ', len(repos))   # 返回的仓库数

repo_first = repos[0]   # 第一个仓库（字典）
print(repo_first)
print('repo_first_len = ', len(repo_first))     # 第一个仓库中Key的个数
for key in sorted(repo_first.keys()):
    print(key)      # 打印第一个仓库的每个key

# 输出第一个仓库的一些基本信息
print('name of first repo = ', repo_first['name'])
print("owner of first repo = ", repo_first['owner']['login']) # repo_first['owner']仍然是字典
print('starts = ', repo_first['stargazers_count'])
print('created_date = ', repo_first['created_at'])
print('repository = ', repo_first['html_url'])
print('updated_date = ', repo_first['updated_at'])
print('description = ', repo_first['description'])

# 使用pygal可视化上述获取所有仓库信息
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

repo_names = []
repo_stars = []
for repo in repos:
    repo_names.append(repo['name'])
    repo_star = {'value': repo['stargazers_count'],
                 'label': repo['description'],
                 'xlink': repo['html_url']
                 }   # value作为纵坐标值，label是鼠标移动到bar时的工具提示，xlink用于给各个bar添加可点击的链接
    repo_stars.append(repo_star)

my_style = LS('#333366', base_style=LCS)    # 样式
my_config = pygal.Config()          # 参数
my_config.x_label_rotation = 45     # 横轴label旋转45度
my_config.show_legend = True        # 图表左上方的图例是否显示
my_config.title_font_size = 24      # 标题字体大小
my_config.label_font_size = 14      # 副标签字体大小
my_config.major_label_font_size = 18    # 主标签字体大小（）
my_config.truncate_label = 15       # 标签字符较长时缩短到15个字符
my_config.show_y_guides = False     # 不显示水平虚线
my_config.width = 1000              # 自定义图表在浏览器中显示的宽度

chart = pygal.Bar(my_config, style = my_style)
chart.title = 'projects on github sorted by stars'  # 标题
chart.x_labels = repo_names
chart.add('各项目的star数', repo_stars)
chart.render_to_file('C:\\Users\\25224\\Desktop\\github_repos.svg')     # 导出到svg文件，浏览器打开


