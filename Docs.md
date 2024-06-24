# Discord Bot Development Tutorial
## Introduction
The bot is use full to perform various operations in discord. It is user defined operation. A bot can be made with many languages like python, javascript...etc. Examples of bots and their action:
- Information Bots
    - These bots are used to just convey information text to users.
    - Bots are usefull to know about the server and the services offered by it.
- Economy bots
    - To simulate a economy like system which is virtual.
    - And users try to buy and sell product as people do in games.
- Ticket Bots
    - Few discussions are not discussed with users over public channels. So new channels are created using this bot.
    - The mechanism is opening a ticket which means a new channel will be created.
    - Somebody will accept a ticket and will respond the queries of the user.
    - This and all happens privately.
- Moderation Bots
    - To keep the community safe and healthy these bot take actions against people who voilate server rules.
    - The action range from warning to kicking or banning the user.

### Why do we need bots?
- In a server of 1000s or 10000s and above members the staff of the server can't moderate the server or perform action.
- So, coded applications called bots are used to do this.

## Topics to be covered
In this tutorial we will cover basic things to make a discord information bot. And importantly also tell about the base structure to make run the bot which could be applied even for huge bots. So, here are the topics we cover:
1. Python Basic before Bot building.
2. Asynchronous Programming in Python Basics
3. Discord Developer Platform
4. Types of Commands
5. Discordpy Library
6. Cogs
7. Using learned Concepts

## Basic Python Concepts

### Docstrings
Docstrings are creative ways to write documentation, whether it be for a function or a class. Writing docstrings can be helpful for referring to what various parts of the code do, even if you look at the code after a long time. Docstrings are simply text covered in `"""`. They should be placed just after the function or class header. Here is an example:

```py
def sum(x, y):
    """
    The sum of two given numbers is calculated and returned.
    """
    return x + y
```

For uniformity of code and proper representation of what is happening, you might use a particular syntax for writing docstrings. Here is an example where parameters and return types are specified:

```py
def sum(x: int = 0, y: int = 0) -> int:
    """
    Function: sum | Description
    =====
    The sum function computes the sum of the two numbers.

    Parameters
    ===
    - x: The first number given.
    - y: The second number given.

    Returns
    ===
    - (int): The sum of the given numbers.
    """
    return x + y
```

To access the documentation of a function or class, use `function_name.__doc__`. Example:

```py
print(sum.__doc__) # Prints all the documentation we have written.
```

### More About Functions
Functions are always callable. You can check if an object is callable using the `callable` function:

```py
print(callable(sum)) # prints True
print(callable(1)) # prints False
```

To access all the parameters a function is receiving, use `locals()` inside the body of the function. It will return a dictionary of variables with their values:

```py
def example_function(a, b):
    print(locals())

example_function(1, 2)
```

Methods starting and ending with `__` are called dunders or magic methods. To get more information about a function, use `function_name.__builtins__`.

You can pass parameters to a function as a list using `*args`:

```py
args = [23, 43]
print(sum(*args)) # returns 66
```

Similarly, you can pass parameters as a dictionary using `**kwargs`:

```py
def sum(x: int, y: int):
    print("x:", x)
    print("y:", y)
    print("Sum is ", x + y)

kwargs = {
    "y": 4,
    "x": 6
}
sum(**kwargs)
```

### Decorators
Decorators are a powerful and useful tool in Python that allows you to modify the behavior of a function or class. They are typically used for logging, access control, instrumentation, and caching.

Here is an example of a simple decorator:

```py
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

In this example, `my_decorator` is a decorator that wraps the `say_hello` function.

### Classes
Classes in Python are a fundamental part of object-oriented programming. They are used to create new user-defined data structures that contain both data and methods. Here is a basic example:

```py
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy", 3)
my_dog.bark()
```

#### Using Classes as Data Structures
Classes can be used to create complex data structures. Here is an example of a linked list:

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.print_list()
```

#### Using Classes for Objects
Classes are used to create objects, which are instances of classes. Each object can have unique values for its properties. Here is an example:

```py
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

my_car = Car("Toyota", "Corolla", 2020)
print(my_car.description())
```

#### Methods
Methods are functions defined within a class. They are used to define the behaviors of an object. Here is an example:

```py
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

my_circle = Circle(5)
print(my_circle.area())
```

#### Important Dunders
Dunder (double underscore) methods are special methods that have double underscores before and after their names. They are also called magic methods. Here are a few important ones:

- `__init__`: Constructor method, called when an instance is created.
- `__str__`: Called by the `str()` function and `print` statement to get the string representation of an object.
- `__repr__`: Called by the `repr()` function to get the string representation of an object.
- `__len__`: Called by the `len()` function to get the length of an object.
- `__getitem__`: Called to get an item from an object.

Example:

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(str(person))  # Alice is 30 years old
print(repr(person)) # Person('Alice', 30)
```

#### `@property`
The `@property` decorator allows you to define methods in a class that can be accessed like attributes. Here is an example:

```py
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(temp.fahrenheit)  # 77.0
```

#### `@staticmethod` and `@classmethod`
`@staticmethod` defines a static method that does not receive an implicit first argument (like `self` or `cls`). `@classmethod` defines a class method that receives the class as its first argument. Here are examples:

```py
class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def mul(cls, x, y):
        return x * y

print(Math.add(5, 3))  # 8
print(Math.mul(5, 3))  # 15
```

#### `@abstractmethod`
`@abstractmethod` is used to define abstract methods in abstract base classes. An abstract method is a method that is declared but contains no implementation. Here is an example:

```py
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

my_dog = Dog()
print(my_dog.sound())
```

In this example, `sound` is an abstract method in the `Animal` class, and it is implemented in the `Dog` class.

By understanding and utilizing these Python concepts, you can write more efficient, readable, and maintainable code.

## Basics of Asynchronous Programing
Synchronous programming is a way to execute a code one after another sequentially or in a synchronous fashion. But, this has limitations like for example you are having a server then you have a lot of requests and tasks to perform and you can't sequentially do tasks there. So, you need to process multiple things simultaneously or somehow atleast simulate that. Let me not go into much details. But, ig you have got the idea. Here, if we choose parallel programming then for 1000 request we need 1000 cores running simultaneously to do concurrent execution of tasks (Assuming that each request is so huge and is handled by 1 core). If we make processes thats expensive and requires time and we get into lot of complexity. If we do this via threads then while sharing information between one thread and another thread we get into trouble and things go too slow there. So we use a concept of running a loop in a perticular manner such that this gets simulated. (Again, not going into technical detials.)

This results in an amazing functionality by which we can simulate concurrent executions. For this task we use a library in python called `asyncio`. You can use `pip install asyncio` or `pip2` or `pip3` instead of `pip` based on what your pc works.
```py
# Each task takes time to execute so lets simulate that time taken by task by time library's sleep method.
import time 
# lets declare 3 functions sequentially and execute.
def cat():
    time.sleep(3)
    print("I am Cat and I am here")
    return "Meow"

def dog():
    time.sleep(3)
    print("I am Dog and I am here.")
    return "Woof"

def wolf():
    time.sleep(3)
    print("I am Wolf and I am here.")   
    return "*Looks these animals*"

cat()
dog()
wolf()
```
Now you can see that their output is not coming at the same time. They are taking time and executing one after the other. Thus, we use asycio to solve this. We do few things here:
    - Before every function which we want to use in asynchronous programming we use `async` keyword before `def function_name`.
    - We will use `await` keyword (called as awaiting) when something is related to getting output or something. (being too vague about this)
    - We will use asyncio's sleep method instead of other sleep methods to facilitate this.
    - You have to make a task for functions to run as tasks using `aysncio.create_task`
    - Then you have to run the asynchronous function with `asyncio.run(main())`
```py
import asyncio

async def cat():
    await asyncio.sleep(3)
    print("I am Cat and I am here")

async def dog():
    await asyncio.sleep(3)
    print("I am Dog and I am here.")

async def wolf():
    await asyncio.sleep(3)
    print("I am Wolf and I am here.")

async def main():
    cat_task = asyncio.create_task(cat())
    dog_task = asyncio.create_task(dog())
    wolf_task = asyncio.create_task(wolf())

    await cat_task
    await dog_task
    await wolf_task

asyncio.run(main())
```
Any shortcut to not repeatedly write `asyncio.create_task`? Yes we have one. We use `asyncio.gather`. And here we pass arguments as functions. Example
```py
import asyncio

async def cat():
    await asyncio.sleep(3)
    print("I am Cat and I am here")

async def dog():
    await asyncio.sleep(3)
    print("I am Dog and I am here.")

async def wolf():
    await asyncio.sleep(3)
    print("I am Wolf and I am here.")

async def main():
    await asyncio.gather(
        cat(),
        dog(),
        wolf()
    )

asyncio.run(main())
```
This even works well for huge tasks and that is why it was made. :wink:

## Discord Developer Platform
Discord has a platform for developers. [Discord Developers Platform](<https://discord.com/developers/applications>) is a site where you can build applications by coding which interact with discord. And help you automate few tasks and even have fun. This is done using libraries which uses API to interact with discord application and then provide things for you as per your code in discord. What do these applications do? These act like users also reffered to as bots. They become online when the code is running. And as per the code they perform actions. The code is a sequence of asynchronous functions. Each function gets triggered with a command. Few commands are used by typing normally a message but having a prefix in them which trigers the command. Other method is syncing it with discord api and telling it that make a setting such that when we type `/` in message field in discord you get the commands (in those as you type command name it shows autocomplete suggestions). These type are generally refered to as slash commands.

Ok. Now lets start making an application first before making it into its functional state. Follow the billow steps:
1. Go to [Discord Developers Platform](<https://discord.com/developers/applications>). You will see the screen like this bellow. ![Dev Portal Image Alt Text](.images/devportal.PNG)
2. On the top right click on new application and give the bot your name.
3. Now here you can fill up name, description and tags as shown there. You see a private information like application id and public key. (This information should not be shared.) ![General Information in Dev Portal image](.images\gen_info.PNG)
4. Other things are not of that much relevance right now. Its important when the application becomes large enough and you have your own site dealing with few of its operations. Next, go to `Installation tab on left hand side of the screen. And in `Install link` select `Discord Provided Link` in dropdown. ![alt text](.images/installation.png)
5. Down you will see `Default Install Settings` in that `Guild Install` in that `Scopes` and there click on the dropdown and select `bot`. (As this application is a bot.) And then you see `Permissions` in that type or select `Administrator`. Note that, this is a very dangerous and powerfull permision so give it to only the bots you trust like your own bot. It has rights to control the server and even see each and every channel. After all this save the changes. Now it should look something like this: [alt text](.images/filled_installation.PNG)
6. And again in the left tab go for `Bot` decide what should be the bot icon (Profile image of bot), bot banner(background image of profile image). And then bellow configure the settings as shown and save changes.![alt text](.images/bot.png)
7. As its first time reset the token and copy it. This is a secret way in which you will communicate the discord API. When ever I refer to Token use this. (In case the token is not working or your token gets shared to another person whom you didn't intend to then reset it.)
8. Now go to your server where you want to invite the bot. (I prefer you to create your own new server for testing purposes.) And there paste the link in some channel. Then click on the link and you will be asked to select the server where you want to invite then authorize (A guided process which you could complete easily) and then bot is added to the server. Alternative thing is for you to search it on browser on which your discord account is logged in. And try it.
> **Note:** The possible error is for few of you it will not be showing your desired server to add bot to. In that case it means that you have no server which has permission to add bot in that. The best thing to get that permission easily is to either request some admin in that server or have your own server in which you default would have permission to add bot there.

After these all you have made a ready application to go ahead and now its offline as there is no code running behind to make it online. In the comming sections, I will tell how to make it online and perform tasks.

## Types of Commands
In the previous sections, I have told you a bit about commands. Here I am going to elaborate it a bit more. This section is going to be short. We have discussed 2 types of commands. And I will make you familiar with even the technical terminologies of it. And also discuss one more types of commands which is hybrid of both the types. Now, lets go forward types of commands.
1. Slash commands
![alt text](.images/slashcmds.PNG)
    - As you can see in the picture, these get triggered by using the slash and following the name of the command. These commands specific to what you are seeing are called buitin commands because it is default given by discord application (aka builtin). And we can define our own bot slash commands which come here.
    - These are also called as application commands as they sync into discord application. And as this is connected to directly discord this has limitations on number of these commands per bot.
    - In these commands there are 2 scopes or area under which they work. Global level syncing of these commmands i.e. they will be visible to all servers (when bot is invited) or guild level syncing which are visible only to a server. Here, guild means another name to refer server.
2. Message Context Commands
![ctx commands image from web](https://cdn-images-1.medium.com/v2/resize:fit:2000/1*z_I0NNJGGBFY8k18WZw1kQ.png)
    - These commands are just focussed on displaying messages in the servers. They don't have much to do with complex operations. 
    - These use prefix to get triggered and operate. Here in the image the triger is the prefix `!`. Meanwhile, you can set your own prefix.
3. Hybrid commands
    - Now its simple to explain this. These are the commands which are both triggered by prefix and slash command in the message field followed by their name.

## Discordpy Library

- There are many libraries out there for dealing with discord api.
- The advantage with the discordpy is it has huge community online using it. So you can easily find help compare to other libraires.
- The disadvantage is the admins in their official server are rude while asking support. (So, I personally ask in other servers for support and its too helpfull.)
- You can install this package using `pip install discord` or `pip3 install discord` based on what works for you.
- The structure of the simple bot is this:
```py
# Import the library to access its functions
import discord
# to use commands 
from discord.ext import commands
```
These libraries are helpful to go further in code. Here we actually can just use `discord.ext.commands` instead of importing it in the second non-commented statement. But we do this for simplicity. Before continuing with the later part of the code I am going to say a small topic refered as intents.
### Intents
These are simple ways/methods to subscribe to certain activity which your bot is allowed to do. These are of two types as shown below.

1. **Gateway Intents**
    - Used to allow bot developers to select events their bot receives based on data needs.
    - Intents are pre-defined WebSocket events that the discord.js client will receive.
    - Enabling all intents can lead to errors, so consider what information is needed.

2. **Privileged Intents**
    - Known as GuildPresences, MessageContent, and GuildMembers.
    - Enabled for bots not verified and in less than 100 guilds.
    - Requested for verified or about to require verification.

```py
# Here we are setting intents to default intents
intents = discord.Intents.default() 
# Can use `discord.Intents.all()` to enable or subscribe to all intents.
intents.message_content = True  # Ensure this intent is enabled if you're using message content
```
The one more thing to discuss a bit before continuing is `discord.Client` class. This is an old class and has a basic features. The class was extended later. And now we use `commands.Bot` class.
```py
# commands.Bot is an extension of discord.Client class with more features in this.
bot = commands.Bot(command_prefix='.', intents=intents)
```
Now lets discuss about events, event handlers and `@bot.event` decorator.
**What is an Event?**

An event is something that happens within Discord that your bot can respond to. Examples of events include:
- A message being sent in a channel.
- A user joining a server.
- The bot successfully connecting to Discord.

**What is an Event Handler?**

An event handler is a function in your bot's code that gets called when a specific event occurs. This function defines how your bot should respond to that event.

But what is `@bot.event` decorator? The `@bot.event` decorator is a way to tell your bot which functions are event handlers. When you use `@bot.event` above a function, you're saying, "This function should run when a certain event happens."
```py
# Here is a decorator which is about events the bot performs.
@bot.event
async def on_ready() -> None:  
    # This asynchronous function representing the event is executed when the bot is ready
    print(f"Logged in as {bot.user.display_name}") # Here bot.user.display_name means the name displayed in the profile of the bot user.

# Similarly another event.
@bot.event
async def on_message(message: discord.Message) -> None: 
    # Note: In all the below things, author refers to the person who triggered the bot.

    # This event lets this function execute on someone sending a message.
    if message.author.bot:  
        # If the message's author is a bot, then do nothing
        return 

    if message.content.lower()=="hi":
        # If the message's author sends 'hi', then send a message in a channel telling 'Hello! Happy to see you here.'
        # Also adding an optional parameter telling to delete the message after 3 seconds (optional parameter)
        await message.channel.send(content="Hello! Happy to see you here.", delete_after=30) 

    
    # Ensure commands are processed
    await bot.process_commands(message)
```
Its important to note that these keep on executing if there is no stopping criteria. For example: Consider if we need to send "This is a user.", if a person is user sends a message. Then, even if, user sends a message context command which has a prefix. The control comes here and the bot still sends "This is a user." text. So, its important to use this carefully. 

The `await bot.process_commands(message)` statement is an important statement. It actually checks if the message is actually a command or not. If it is a command it allows it to get processed as a command. If you don't write this statement then it doesn't process it as a command.
```py
# similar to event, now we are making a command the below decorator
@bot.command()
async def say(ctx: commands.Context, message: str) -> None:  
    """
    Function: say | Description
    =====
    It mentions the user first. This is done by getting the author's userID by commands.Context class.
    And then '.mention' method takes the userID and mentions the user. Example: @user_name
    I personally guess this is done by adding a string as '<@user_id_here>'.
    And then message is displayed in the next line. '> ' is used to display it as quoted.

    Parameters
    ===
    - (Here commands.Context is automatically taken as you trigger the bot.) 
    - message: This is a string representing the message you write.

    Returns
    ===
    Keeping the triggering message you sent in context, it sends you the message in whichever channel triggered it there itself.
    """
    await ctx.send(f"{ctx.author.mention} says, \n> {message}")
```
The above is a command. Whenever we trigger using the prefix we get this asynchronous function get executed here. And this is my style of writing documentation. And ig its self explanatory over what is happening. After this step you just run the bot. That is done by:
```py
bot.run("PASTE YOUR COPIED TOKEN HERE")
```
Here we are talking about the same bot token which we got from discord developer portal by reseting it (Mentioned in Discord Developer Portal section in step 7). Now after explain the code by parts this is the whole code without comments:
```py
import discord
from discord.ext import commands

intents = discord.Intents.default() 
intents.message_content = True  
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready() -> None:  
    print(f"Logged in as {bot.user.display_name}")

@bot.event
async def on_message(message: discord.Message) -> None: 
    if message.author.bot:  
        return 

    if message.content.lower()=="hi":
        await message.channel.send(content="Hello! Happy to see you here.", delete_after=30) 

    await bot.process_commands(message)

@bot.command()
async def say(ctx: commands.Context, message: str) -> None:  
    await ctx.send(f"{ctx.author.mention} says, \n> {message}")

bot.run("PASTE YOUR COPIED TOKEN HERE")
```
Now you can try it out making your commands in different ways. If you are wondering to add a slash commands this is how it is done.
```py
from discord import app_commands # New thing to be imported.
from random import choice
import discord
from discord.ext import commands

intents = discord.Intents.default() 
intents.message_content = True  
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready() -> None:  
    print(f"Logged in as {bot.user.display_name}")

@bot.event
async def on_message(message: discord.Message) -> None: 
    if message.author.bot:  
        return 

    if message.content.lower() == "hi":
        await message.channel.send(content="Hello! Happy to see you here.", delete_after=30) 

    await bot.process_commands(message)

@bot.command()
async def say(ctx: commands.Context, message: str) -> None:  
    await ctx.send(f"{ctx.author.mention} says, \n> {message}")

# This is our app command. Note that the decorator is different here. And it's taking arguments.
@app_commands.command(name="toss", description="Tosses a coin and tells heads or tails.")
async def toss(inter: discord.Interaction):  # The async function to execute when triggered.
    # This uses discord.Interaction object as we are interacting with discord Application more directly in this.

    # randomly picks a string
    result = choice(["Heads", "Tails"])
    # The interaction's response to send a message is written as follows:
    await inter.response.send_message(result)


# Command to remove the 'toss' command
@bot.command()
async def unsync(ctx: commands.Context):

    # We need to sync or unsync commands in this guild so use obtain it as follows
    guild=ctx.guild # getting guild objects 
    GUILD_ID=ctx.guild.id # getting guild id

    try:
        bot.tree.remove_command(toss.name, guild=guild)
        await ctx.send(f"Command 'toss' removed from guild {GUILD_ID}")
    except KeyError:
        await ctx.send(f"Command 'toss' not found in guild {GUILD_ID}")

# Command to re-sync the command tree
@bot.command()
async def sync(ctx: commands.Context):

    # We need to sync or unsync commands in this guild so use obtain it as follows
    guild=ctx.guild # getting guild objects 
    GUILD_ID=ctx.guild.id # getting guild id

    try:
        bot.tree.add_command(toss, guild=guild)
        await bot.tree.sync(guild=guild)
        await ctx.send(f"Command 'toss' added and synced to guild {GUILD_ID}")
    except discord.app_commands.CommandAlreadyRegistered:
        await ctx.send(f"Command 'toss' already registered in guild {GUILD_ID}")
    await bot.tree.sync(guild=guild)

bot.run("PASTE YOUR COPIED TOKEN HERE")
```
Explaining a bit of what I did, Firstly, I made the command using application commands command method and then it has a async function which gets executed. And then I added two message context commands. This helps me to operate from discord message field and control the code. So, one is for syncing the toss application command in bot's tree of commands on the guild where bot was triggered to sync. I got to know the guild where the bot was triggered by using `ctx.guild` method. This gave me the guild or server object. And then I can extract server id by telling `ctx.guild.id`. Finaly I used add command to first add it to bot's tree of commands. And then what I did was to sync the tree in discord's api. This final things shows api what is our new structure. Similarly I removed the application command. Here, I used try and except clauses because if the command is already synced/ registered or in other case command is not there which I am removing it displays the messages as show above.

## Cogs
While working with a huge bot you would need the code of things to be in different files. This helps in modular level of working in the software. And it even increases the productivity. It would be messy if we writing all or many lines of code in a single file. This is done using concept called **Cogs**. I have personally made the file structure of it [here](<https://github.com/WuiiiGithub/discordbot_python/files/templates/cogs_template>). You can modify and treat it as a template for your work.

## Using Learned Concepts
Will be discussing later.