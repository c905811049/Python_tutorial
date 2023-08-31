'''
继承是面向对象编程的核心概念之一，它允许新类（子类）从现有类（父类）继承属性和方法。这有助于促进代码重用和创建清晰的类层次结构。

### 3.1 基本继承

子类通过继承父类来获取父类的所有属性和方法。

#### 示例：动物和哺乳动物

```Python
class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal): # 继承Animal类
    def speak(self):
        print("Mammal speaks")

mammal = Mammal()
mammal.speak() # 输出："Mammal speaks"
```


### 3.2 方法重写

如果子类需要以特殊方式实现父类的某个方法，可以在子类中重新定义该方法。这称为方法重写。

#### 示例：狗类重写说话方法

```Python
class Dog(Mammal): # 继承Mammal类
    def speak(self):
        print("Woof! Woof!")

dog = Dog()
dog.speak() # 输出："Woof! Woof!"
```


### 3.3 调用父类方法（`super`）

在重写方法时，你可能还想调用父类的原始实现。可以使用`super`函数做到这一点。

#### 示例：调用父类的说话方法

```Python
class Cat(Mammal): # 继承Mammal类
    def speak(self):
        super().speak() # 调用父类的speak方法
        print("Meow! Meow!")

cat = Cat()
cat.speak()
# 输出：
# Mammal speaks
# Meow! Meow!
```


### 3.4 多重继承

Python支持多重继承，这意味着一个类可以从多个父类继承。

#### 示例：多重继承

```Python
class Swimming:
    def swim(self):
        print("Swimming")

class Flying:
    def fly(self):
        print("Flying")

class Bird(Swimming, Flying): # 从多个类继承
    pass

bird = Bird()
bird.swim() # 输出："Swimming"
bird.fly() # 输出："Flying"
```


### 继承的好处

1. **代码重用**：通过继承共同特征，你可以避免重复代码。

2. **可扩展性**：你可以通过创建新的子类来扩展现有类的功能，而不必修改现有代码。

3. **组织结构**：通过创建类层次结构，你可以在概念上组织代码，使之更易于理解和维护。

继承是OOP中的强大工具，有助于创建清晰、可维护的代码。


'''