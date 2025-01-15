# Module > Method
# 1. import random => random => module
# 2. random.randint => randint => method

# __name__
# 1. __name__ = __main__ 
# 2. احنا بنستخدمها علشان نعرف هل الكود شغال من الصفحة الرئيسية المكتوب فيها الكود ولا معموله import لصفحة كود تانيه.
# 3. لما يشتغل الكود من صفحته الاصلية المكتوب فيها الكود بيبقى => __name__ = __main__
# 4. لما يشتغل الكود من صفحة تانيه عن طريق import => __name__ != __main__

# Timeit => import timeit => معرفة اقل مدة زمنيه لتكرار فعل امر ما عدد محدد من المرات
# 1. طباعة اقل زمن يستغرقه تكرار كلمة محددة عدد محدد من المرات
# Order don't need import => print(timeit.timeit("name = 'Basel'; name * 1000"))
# Order need import => print(timeit.timeit(stmt= "random.randint(0, 50)", setup= "import random"))
# 2. تكرار اول عمليه اللي هي رقم واحد عدد محدد من المرات ومعرفة اقل زمن في كل مرة => print(timeit.timeit(stmt= "random.randint(0, 50)", setup= "import random", repeat=4))