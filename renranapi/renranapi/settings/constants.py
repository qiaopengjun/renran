# 常量配置文件
# 这里的所有信息,线上线下都一样
# 短信有效期[单位: s]
SMS_EXPIRE_TIME = 10 * 60
# 短信发送间隔[单位: s]
SMS_INTERVAL_TIME = 60

DATA_SIGNATURE_EXPIRE = 300
# 首页轮播图显示个数
HOME_BANNER_LENGTH = 10
# 头部顶级导航数量
HEADER_NAV_LENGTH = 8
# 脚部顶级导航数量
FOOTER_NAV_LENGTH = 8
# Feed流系统的分区键
RELATION_TABLE_ID = 1   # 关系表的分区键
MESSAGE_TABLE_ID = 1   # 同步库的分区键
# 行为日志的分区键
LOG_TABLE_ID = 1
# 首页文章推荐度
CF_READ = 1     # 阅读文章的推荐度
CF_LIKE = 2     # 点赞文章的推荐度
CF_COMMENT = 5   # 评论文章的推荐度
CF_REWARD = 10  # 打赏文章的推荐度
