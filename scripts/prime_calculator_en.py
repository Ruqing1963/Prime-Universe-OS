import sys
import time

try:
    import sympy
except ImportError:
    print("[!] FATAL ERROR: SymPy library is missing.")
    print("    Please install it by running: pip install sympy")
    sys.exit(1)

# =====================================================================
# SYSTEM CONSTANTS & COSMIC LAWS
# =====================================================================
# The event horizon restricts calculations of massively large primes
# due to computational limits of the prime-counting function pi(x).
COMPUTATIONAL_EVENT_HORIZON = 10**12 

def typewriter_print(text, delay=0.01):
    """Simulates terminal typewriter effect for immersion."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def enforce_cosmic_law(val):
    """Checks if the prime exceeds the computational event horizon."""
    if val > COMPUTATIONAL_EVENT_HORIZON:
        print("\n" + "!"*60)
        print("⚠️ [COSMIC LAW VIOLATION] ENERGY LEVEL TOO HIGH!")
        print(f"The entity {val} exceeds the OS Event Horizon ({COMPUTATIONAL_EVENT_HORIZON}).")
        print("Attempting to process this would cause a temporal paradox (infinite loop).")
        print("Aborting operation to protect the space-time continuum.")
        print("!"*60 + "\n")
        return False
    return True

def interactive_calculator():
    print("="*65)
    typewriter_print("🌌 PRIME-UNIVERSE OS [Terminal v2.1]")
    print("Axiom: p_1=2, p_2=3, p_3=5, p_4=7, p_5=11 ... p_i = the i-th prime")
    print("="*65)
    
    while True:
        print("\n" + "-"*55)
        print("💡 SELECT PRIME OPERATION PROTOCOL:")
        print("  [1] Prime Addition (⊕)       : Dimensional Superposition")
        print("  [2] Prime Multiplication (⊗) : Dimensional Leap")
        print("  [3] Prime Subtraction (⊖)    : Gravitational Decay")
        print("  [4] Self-Reference Fold (J)  : Super-Prime Generator")
        print("  [0] Exit OS")
        
        choice = input("\n👉 Enter protocol number (0-4): ").strip()
        
        if choice == '0':
            typewriter_print("🌌 Exiting Prime-Universe. Returning to the real world. Farewell, Captain!")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("⚠️ VOID ALERT: Invalid protocol. Please re-enter.")
            continue
            
        try:
            # Handle binary operations (Addition, Multiplication, Subtraction)
            if choice in ['1', '2', '3']:
                val_i = int(input("Enter the first prime entity (pi): ").strip())
                val_j = int(input("Enter the second prime entity (pj): ").strip())
                
                # Check 1: Are they primes?
                if not (sympy.isprime(val_i) and sympy.isprime(val_j)):
                    print("⚠️ VOID COLLAPSE: Composite number or anomaly detected!")
                    print("   Only pure primes can exist in this universe.")
                    continue
                
                # Check 2: Cosmic Law (Performance Limit)
                if not (enforce_cosmic_law(val_i) and enforce_cosmic_law(val_j)):
                    continue
                    
                # Extract absolute index (pi function)
                idx_i = sympy.primepi(val_i)
                idx_j = sympy.primepi(val_j)
                
                print(f"\n[*] Coordinates Resolved: p_{idx_i} = {val_i} | p_{idx_j} = {val_j}")
                
                if choice == '1':
                    res_idx = idx_i + idx_j
                    res_val = sympy.prime(res_idx)
                    print(f"✨ [ADDITION YIELD] {val_i} ⊕ {val_j} Derivation:")
                    print(f"   p_{idx_i} ⊕ p_{idx_j}  =>  p_{idx_i}+{idx_j}  =>  p_{res_idx} = {res_val}")
                    
                elif choice == '2':
                    res_idx = idx_i * idx_j
                    # Safe-guard for massive multiplication bounds
                    if enforce_cosmic_law(res_idx):
                        res_val = sympy.prime(res_idx)
                        print(f"✨ [MULTIPLICATION YIELD] {val_i} ⊗ {val_j} Derivation:")
                        print(f"   p_{idx_i} ⊗ p_{idx_j}  =>  p_{idx_i}×{idx_j}  =>  p_{res_idx} = {res_val}")
                    
                elif choice == '3':
                    if idx_i <= idx_j:
                        print(f"⚠️ DECAY FAILED: The energy of p_{idx_i} must be strictly greater than p_{idx_j}!")
                        print("   Otherwise, the entity collapses into the non-positive integer void.")
                        continue
                    res_idx = idx_i - idx_j
                    res_val = sympy.prime(res_idx)
                    print(f"✨ [SUBTRACTION YIELD] {val_i} ⊖ {val_j} Derivation:")
                    print(f"   p_{idx_i} ⊖ p_{idx_j}  =>  p_{idx_i}-{idx_j}  =>  p_{res_idx} = {res_val}")
                    
            # Handle unary operation (Self-Reference Fold)
            elif choice == '4':
                val_i = int(input("Enter the prime entity to fold (pi): ").strip())
                
                if not sympy.isprime(val_i):
                    print("⚠️ VOID COLLAPSE: The entered entity is not a prime!")
                    continue
                
                if not enforce_cosmic_law(val_i):
                    continue
                    
                idx_i = sympy.primepi(val_i)
                print(f"\n[*] Coordinates Resolved: p_{idx_i} = {val_i}")
                
                # Super-prime logic: The prime value itself becomes the new index
                res_val = sympy.prime(val_i)
                print(f"✨ [FOLDING YIELD] J({val_i}) Derivation:")
                print(f"   Extracting the {val_i}-th prime  =>  p_{val_i} = {res_val}")
                
        except ValueError:
            print("⚠️ SYSTEM FAULT: Invalid format. Please ensure you enter pure integers.")

if __name__ == "__main__":
    interactive_calculator()