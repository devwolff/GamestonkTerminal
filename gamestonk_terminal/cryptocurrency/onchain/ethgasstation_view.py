"""ETH Gas Station view"""
import os

from gamestonk_terminal.helper_funcs import export_data, print_rich_table
from gamestonk_terminal.cryptocurrency.onchain.ethgasstation_model import get_gwei_fees
from gamestonk_terminal.rich_config import console


def display_gwei_fees(export: str) -> None:
    """Current gwei fees
    [Source: https://ethgasstation.info]

    Parameters
    ----------
    export : str
        Export dataframe data to csv,json,xlsx file
    """

    df_fees = get_gwei_fees()

    if df_fees.empty:
        console.print("\nError in ethgasstation request\n")
    else:
        console.print("\nCurrent ETH gas fees (gwei):")

        print_rich_table(
            df_fees.head(4),
            headers=list(df_fees.columns),
            show_index=False,
            title="Current GWEI Fees",
        )
        console.print("")

        export_data(
            export,
            os.path.dirname(os.path.abspath(__file__)),
            "gwei",
            df_fees,
        )
