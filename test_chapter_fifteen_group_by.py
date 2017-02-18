# coding=utf-8

'''

使用group by

要遵循单值规则：

属于每个组的行， 他们的group by关键字所指定的那些列中的值都是一样的。
例如：
select product_id , max(date_reported)
from bugs join BugsProducts using (bug_id)
group by product_id


跟在select之后的选择列表中的每一列，对于每个分组来说都必须返回且仅返回一个值。
在group by字句中出现的列能够保证他们在每一组都只有一个值，无论这个值匹配了多少行
product_id, date_reported
1         , 2001-2-1
1         , 2001-2-2
1         , 2001-2-3
1         , 2001-2-4
Max()表达式也能保证每组都返回单一的值。

所以：

select product_id , max(date_reported), bug_id
from bugs join BugsProducts using (bug_id)
group by product_id

这里数据库不能确定其他的那些在选择列表中的列都是单值的。这个例子中，
一个给定的product_id有很多不同的bug_id，因为BugsProducts表将很多Bug
和同一个产品关联起来。在一个根据product_id进行分组的查询中，数据库没办法在查询
结果中表示所有的bug_id


----------------------
1` 只查询功能依赖的列

select product_id , max(date_reported)
from bugs join BugsProducts using (bug_id)
group by product_id

2` 使用关联子查询

select b1.product_id, b1.date_reported, b1.bug_id
from Bugs b1 join BugsProducts bp1 USING (bug_id)
where not exists (
    select * from Bugs b2 join BugsProducts bp2 USING(bug_id)
    where bp1.product_id = bp2.product_id
      and b1.date_reported < b2.date_reported

)

'''
