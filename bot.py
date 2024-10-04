import requests
from colorama import Fore, Style, init

# Inisialisasi colorama untuk pewarnaan terminal
init(autoreset=True)

def check_airdrop_allocation(wallet_address):
    url = "https://api.getgrass.io/airdropAllocationsV2"
    
    # Parameter query string
    params = {
        "input": f'{{"walletAddress":"{wallet_address}"}}'
    }
    
    # Mengirim permintaan GET
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # Mengecek apakah data respons berisi alokasi sybil
        if 'result' in data and 'data' in data['result']:
            allocations = data['result']['data']
            
            # Menghitung total alokasi koin
            total_allocation = sum(allocations.values())
            
            # Jika total alokasi lebih dari 0, wallet eligible
            if total_allocation > 0:
                return True, total_allocation
            else:
                return False, 0
        else:
            return False, 0
    else:
        return False, 0

def check_wallets_from_file(file_path):
    total_allocation_all_wallets = 0  # Variabel untuk menyimpan total alokasi semua wallet
    eligible_wallets = 0  # Variabel untuk menghitung jumlah wallet yang eligible

    try:
        with open(file_path, 'r') as file:
            wallets = file.readlines()
            
            for wallet in wallets:
                wallet = wallet.strip()  # Menghapus spasi putih atau newline
                if wallet:
                    eligible, total_allocation = check_airdrop_allocation(wallet)
                    
                    # Jika wallet eligible, tampilkan dalam warna hijau
                    if eligible:
                        total_allocation_all_wallets += total_allocation
                        eligible_wallets += 1
                        print(f"{Fore.GREEN}Wallet: {wallet} - Eligible. Total alokasi: {total_allocation} coins.")
                    # Jika tidak eligible, tampilkan dalam warna merah
                    else:
                        print(f"{Fore.RED}Wallet: {wallet} - Not eligible for any allocation.")
        
        # Menampilkan total alokasi koin dari semua wallet di akhir
        print(f"\n{Fore.YELLOW}Total alokasi koin semua wallet: {total_allocation_all_wallets} coins.")
        print(f"{Fore.CYAN}Total wallet eligible: {eligible_wallets} dari {len(wallets)} wallet.")
    
    except FileNotFoundError:
        print(f"{Fore.RED}File {file_path} tidak ditemukan.")
    except Exception as e:
        print(f"{Fore.RED}Terjadi kesalahan: {str(e)}")

# Contoh penggunaan:
file_path = "wallet.txt"  # Nama file yang berisi daftar wallet
check_wallets_from_file(file_path)
