from django.db import models

# 学生
class Student(models.Model):
    """学生模型"""
    """学生模型"""
    id = models.BigAutoField(primary_key=True)  # 自动递增的主键字段，通常与 bigint 对应
    name = models.CharField(max_length=100, verbose_name="姓名")  # 不允许为空的字符串字段
    gender = models.SmallIntegerField(verbose_name="性别")  # 不允许为空的整数字段

    class Meta:
        db_table = "student"
        verbose_name = "学生"
        verbose_name_plural = "学生"


# 老师
class Teacher(models.Model):
    id = models.BigAutoField(primary_key=True)  # Auto-incrementing primary key, corresponding to bigint
    name = models.CharField(max_length=100)  # Corresponds to varchar(100) in SQL

    class Meta:
        db_table = "teacher"
        verbose_name = "老师"
        verbose_name_plural = "老师"

# 课程
class Course(models.Model):
    id = models.BigAutoField(primary_key=True)  # Django uses BigAutoField for auto-incrementing primary keys
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)  # Set null if teacher is not required

    class Meta:
        db_table = "course"
        verbose_name = "课程"
        verbose_name_plural = "课程"

# 成绩
class Grade(models.Model):
    number = models.FloatField()  # 使用 FloatField 对应 SQL 中的 double
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # 外键关联 Course
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # 外键关联 Student

    class Meta:
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'
        db_table = 'grade'  # 指定数据库表名

    def __str__(self):
        return f'Grade {self.number} for {self.student} in {self.course}'


# 学生选课结果
class StudentCourseGroup(models.Model):
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)  # 外键关联 Student
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)  # 外键关联 Course
    class Meta:
        verbose_name = 'Student Course Group'
        verbose_name_plural = 'Student Course Groups'
        db_table = 'student_course_group'  # 指定数据库表名

    def __str__(self):
        return f'{self.student} - {self.course}'



