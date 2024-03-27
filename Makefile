.PHONY: install clean

MINIFUZZT_DIR := src
INSTALL_DIR := $(HOME)/.local/bin/minifuzz/


GREEN := \033[0;32m
NC := \033[0m

all: minifuzz 

reinstall: uninstall clean all install

minifuzz:
	cd $(MINIFUZZT_DIR) && pyinstaller minifuzz.spec

install:
	@echo "\n$(GREEN)>>> Application installing!$(NC)"
	mkdir -p $(INSTALL_DIR)
	cp $(MINIFUZZT_DIR)/dist/minifuzz/* -a $(INSTALL_DIR)
	echo 'export PATH="$(INSTALL_DIR):$$PATH"' >> $(HOME)/.bashrc
	@echo "$(GREEN)Application installed successfully!$(NC)"
	@echo "$(GREEN)Please reopen your terminal or run 'source ~/.bashrc' to make the changes effective.$(NC)"


uninstall:
	@echo "\n$(GREEN)>>> Application removing!$(NC)"
	sed -i '\|$(INSTALL_DIR)|d' ~/.bashrc
	rm -rf $(INSTALL_DIR)
	@echo "$(GREEN)Application removed from PATH in ~/.bashrc$(NC)"
	@echo "$(GREEN)Please reopen your terminal or run 'source ~/.bashrc' to make the changes effective.$(NC)"

clean:
	@echo "\n$(GREEN)>>> Application clean!$(NC)"
	cd $(MINIFUZZT_DIR) && rm -rf dist build
