1、a、UI校验
    b、功能测试：
        （发送视频）
        本地相册选择还是直接拍摄
        视频秒数验证：1 - 10s，超出10s
        视频个数验证1个
        视频格式验证
        支持的视频格式
        不支持的视频格式
        最后发送视频，是否可以正常观看（包括自己、朋友）

        （朋友圈点赞)
        点赞成功
        点赞后取消点赞
        弱网情况下点赞
        没网情况下点赞
        点赞后评论
        点赞后消息列表的显示（是按时间还是昵称）
        点赞后共同好友可以看到
        点赞显示行
        一行可以显示多少人
        点赞人数限制
        点赞显示行的排列
        点赞显示行头像的显示
        点暂是手机故障

        （评论功能）
        网速对评论的影响
        共同好友是否能看得到评论
        评论能否按时间先后顺序显示
        评论能否显示评论人的昵称
        若能显示是否正确
        能否回复评论
        是否既点赞又评论
        评论的字数是否有上限
        能否及时刷新
        不同手机如何显示的
        能否将评论全部显示在朋友圈下面
        好友能否看到发圈人的评论及回复
    c、性能测试
        服务端性能测试
        客户端性能测试
    d、兼容性测试
        主要从不同系统、厂商、分辨率、网络对以上功能进行测试
    e、安全性测试
        服务端接口的加密或反编译的测试
        客户端对应接口的容错性测试


2、from collections import Counter
str="adchhaboooabfh"
list = dict(Counter(str))
print({key:value for key,value in list.items() if value > 1})

3、
    1）
        select * from (select top 9* from (select top 20* from Student order by score asc) as a order by score desc)as b order by score asc;
        select top 9* from (select top 20* from Student order by score asc) as a order by score desc
    2)
        索引无法存储null值、不适合键值较少的列（重复数据较多的列）、模糊查询不能利用索引(like '%XX'或者like '%XX%')
