# you can pick with or without eval!
#   with <3, Josh
# Python 2.7.x

# no eval, 171 chars
#print(lambda s,o:[o[k](*(int(a)for a in s.split(k)if a))for k in o if k in s][-1])(raw_input(),{'+':int.__add__,'-':int.__sub__,'*':int.__mul__,'/':int.__div__,'**':pow})

# eval, 160 chars
print(lambda s,**o:[eval('int.__%s__'%k)(*(int(a)for a in s.split(o[k])if a))for k in o if o[k]in s][-1])(raw_input(),add='+',sub='-',mul='*',div='/',pow='**')
