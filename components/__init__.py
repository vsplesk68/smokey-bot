import components.commands
import components.inlinequeries
import components.messagehandlers


def register(dp):
    components.commands.register(dp)
    components.inlinequeries.register(dp)
    components.messagehandlers.register(dp)
