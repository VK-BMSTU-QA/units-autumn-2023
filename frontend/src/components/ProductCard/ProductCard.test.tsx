import { ProductCard } from "./ProductCard";
import { render } from "@testing-library/react";

describe('Product cards test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard
            id={1}
            name="IPhone 14 Pro"
            description="Latest iphone, buy it now"
            price={999}
            priceSymbol="$"
            category="Электроника"
            imgUrl="iphone.png"
        />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});
