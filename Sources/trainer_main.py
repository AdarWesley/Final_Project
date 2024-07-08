from Trainer import Trainer
from Models.trainerModel import TrainerModel
from Views.trainerView import TrainerView
from Controllers.trainerController import TrainerController
from Network.network import Network
from Views.root import Root


def main():
    net = None # change to loadNetwork() according to dropdown menu

    root = Root()
    model = TrainerModel(net)
    view = TrainerView(root, model)
    trainer = Trainer(model)
    controller = TrainerController(model, view, trainer)
    view.tkraise()
    root.mainloop()


if __name__ == '__main__':
    main()