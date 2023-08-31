'''
封装是面向对象编程的关键概念之一，它涉及将对象的状态和行为捆绑在一起，并隐藏内部工作机制的细节。

### 2.1 私有属性和方法

在Python中，你可以通过在变量名或方法名前加上双下划线`__`来表示它们是私有的。这意味着它们不能从类的外部直接访问。

```Python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # 私有属性

    def __display_balance(self): # 私有方法
        print(f"Balance: {self.__balance}")

    def show_balance(self):
        self.__display_balance() # 可以在类的内部访问

account = BankAccount(1000)
account.show_balance() # 输出："Balance: 1000"
# account.__display_balance() # 错误！外部不能访问
```


### 2.2 Getter和Setter方法

如果你想控制对属性的访问和修改，可以使用getter和setter方法。

```Python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self): # Getter
        return self.__balance

    def set_balance(self, balance): # Setter
        if balance < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = balance

account = BankAccount(1000)
print(account.get_balance()) # 输出：1000
account.set_balance(-500) # 输出："Balance cannot be negative!"
```


### 2.3 属性装饰器（`@property`、`@attribute.setter`等）

你还可以使用属性装饰器来更优雅地实现getter和setter。

```Python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self): # Getter
        return self.__balance

    @balance.setter
    def balance(self, balance): # Setter
        if balance < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = balance

account = BankAccount(1000)
print(account.balance) # 输出：1000
account.balance = -500 # 输出："Balance cannot be negative!"
```


### 封装的好处

1. **信息隐藏**：封装允许你隐藏对象的内部状态和实现细节，使外部代码不必了解这些细节。

2. **增强安全性**：通过限制对内部属性的直接访问，你可以防止外部代码误用或破坏对象的状态。

3. **灵活性和可维护性**：你可以自由更改内部实现，而不会影响使用该类的代码。

封装是OOP中的基本原则之一，有助于提高代码的可读性、可维护性和健壮性。
'''