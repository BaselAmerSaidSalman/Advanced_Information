# Module > Method
# 1. import random => random => module
# 2. random.randint => randint => method



# __name__
# 1. __name__ = __main__ 
# 2. احنا بنستخدمها علشان نعرف هل الكود شغال من الصفحة الرئيسية المكتوب فيها الكود ولا معموله import لصفحة كود تانيه.
# 3. لما يشتغل الكود من صفحته الاصلية المكتوب فيها الكود بيبقى => __name__ = __main__
# 4. لما يشتغل الكود من صفحة تانيه عن طريق import => __name__ != __main__

# Example of __name__
if __name__ == "__main__":
    print("This message is showed when you run code directly")
else:
    print("This message is showed when you make import to another code page & run it not directly")



# Timeit => import timeit => معرفة اقل مدة زمنيه لتكرار فعل امر ما عدد محدد من المرات
# 1. طباعة اقل زمن يستغرقه تكرار كلمة محددة عدد محدد من المرات
# Order don't need import => print(timeit.timeit("name = 'Basel'; name * 1000"))
# Order need import => print(timeit.timeit(stmt= "random.randint(0, 50)", setup= "import random"))
# 2. تكرار اول عمليه اللي هي رقم واحد عدد محدد من المرات ومعرفة اقل زمن في كل مرة => print(timeit.timeit(stmt= "random.randint(0, 50)", setup= "import random", repeat=4))

# Example of Timeit
import timeit
print(timeit.timeit("name = 'Basel'; name * 1000")) # don't need import
print(timeit.timeit(stmt= "random.randint(0, 50)", setup= "import random")) # need import
print(timeit.timeit(stmt= "random.randint(0, 50)", setup= "import random", repeat=4))



# Logging => import logging => save all errors, debugs, criticals, warning messages in one file with their times & dates 
# 1. logging.basicConfig(filename="file_name.log", filemode="a to append or w to delete all without last one", format="%(asctime)s => %(name)s => %(levelname)s => %(message)s") => طباعة الاوامر داخل الملف المكتوب اسمه
# 2. variable1 = logging.getLogger("Basel") => name = Basel => without this message => name = root
# 3. Last message (critical, warning, debuging, error) = levelname
# 4. Critical Message => my_logger.critical("This is critical message")
# 5. Warning Message => my_logger.warning("This is warning message")
# 6. Debuging Message => my_logger.debug("This is debuging message")
# 7. Error Message => my_logger.error("This is error message")
# 8. (asctime = time & date), (name = root or your special name that you wrote in variable1), (levelname = critical, error, debug, warning), (message = levelname messages)

# Example of Logging
import logging
logging.basicConfig(filename="app.log", filemode="a", format="%(asctime)s => %(name)s => %(levelname)s => %(message)s")
my_logger = logging.getLogger("Basel")
my_logger.critical("This is a critical message")



# Unit Testing => import unittest => Test something in your code
# 1. create class to test all things that you want to test it in your code with unittest.TestCase parameter => class TestCode(unittest.TestCase):
# 2. create functions in the class to test what you want with self parameter
# 3. put this line in your functions => self.assert => choose what you want (assertGreater, assertEqual or others)
# 4. run your test class => if __name__ == "__main__": => unittest.main()

# Examples of Unit Testing
import unittest
class TestCode(unittest.TestCase):
    def test_one(self):
        self.assertGreater(100, 90, "First Number Should Be Greater Than Second Number")

if __name__ == "__main__":  # this code run only when your run it directly
    unittest.main()






