"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.user_info_route import user_info_bp
    from .orders.user_account_route import user_account_bp
    from .orders.follower_route import follower_bp
    from .orders.statistic_route import statistic_bp
    from .orders.storie_route import storie_bp
    from .orders.media_route import media_bp
    from .orders.views_route import views_bp
    from .orders.reactions_route import reactions_bp
    from .orders.report_route import report_bp

    app.register_blueprint(user_info_bp)
    app.register_blueprint(user_account_bp)
    app.register_blueprint(follower_bp)
    app.register_blueprint(statistic_bp)
    app.register_blueprint(storie_bp)
    app.register_blueprint(media_bp)
    app.register_blueprint(views_bp)
    app.register_blueprint(reactions_bp)
    app.register_blueprint(report_bp)

